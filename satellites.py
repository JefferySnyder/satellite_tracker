from skyfield.api import load, wgs84

def print_list(list):
    for l in list:
        print(l)

def get_sat_info():
    stations_url = 'http://celestrak.org/NORAD/elements/stations.txt'
    satellites = load.tle_file(stations_url)
    # print('Loaded', len(satellites), 'satellites')

    by_name = {sat.name: sat for sat in satellites}
    # print(satellite)

    ts = load.timescale()
    t = ts.now()
    # print(t.utc)

    days = t - by_name['ISS (ZARYA)'].epoch
    # print('{:.3f} days away from epoch'.format(days))

    if abs(days) > 14:
        satellites = load.tle_file(stations_url, reload=True)

    tucson = wgs84.latlon(+32.2540, -110.9742)
    t0 = ts.utc(t.utc.year, t.utc.month, t.utc.day, t.utc.hour - 7)
    t1 = ts.utc(t.utc.year, t.utc.month, t.utc.day + 1, t.utc.hour-7)

    event_names = ['rise above 30°', 'culminate', 'set below 30°']

    res = []
    everyThree = []

    for satellite in satellites:
        t, events = satellite.find_events(tucson, t0, t1, altitude_degrees=30.0)

        eph = load('de421.bsp')
        sunlit = satellite.at(t).is_sunlit(eph)

        for ti, event, sunlit_flag in zip(t, events, sunlit):
            # time = "{}-{}-{} {}:{}:{}".format(ti.utc.year, ti.utc.month, ti.utc.day, ti.utc.hour, ti.utc.minute, int(ti.utc.second))

            event_name = event_names[event]
            state = 'in sunlight' if sunlit_flag else 'in shadow'
            if ti.utc.hour > 21 or ti.utc.hour < 5:
                everyThree.append(
                    [ti.utc_strftime('%Y %b %d at %H:%M:%S'), satellite.name, event_name, state]
                )
        if everyThree:
            res.append(everyThree)
            everyThree = []
    

    res.sort()

    flat_list = [num for sublist in res for num in sublist]
    # print_list(flat_list)        

    # print_list(res)

    return res

get_sat_info()
