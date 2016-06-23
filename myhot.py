import hotshot, hotshot.stats

module = __import__('hello_world')

prof = hotshot.Profile('hello_world.prof')
prof.runcall(module.main)
prof.close()

state = hotshot.stats.load('hello_world.prof')
state.strip_dirs()
state.sort_stats('time', 'calls')
state.print_stats()

