import hotshot, hotshot.stats
from csv_reader import my_simple_reader as mymodule

prof = hotshot.Profile('my_simple_reader.prof')
prof.runcall(mymodule.main)
prof.close()

state = hotshot.stats.load('my_simple_reader.prof')
state.strip_dirs()
state.sort_stats('time', 'calls')
state.print_stats(10)

