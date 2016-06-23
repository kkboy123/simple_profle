import hotshot, hotshot.stats
from csv_reader import my_pandas as mypd

prof = hotshot.Profile('my_pandas.prof')
prof.runcall(mypd.main)
prof.close()

state = hotshot.stats.load('my_pandas.prof')
state.strip_dirs()
state.sort_stats('time', 'calls')
state.print_stats(10)

