import pstats

p = pstats.Stats('outfile')
p.strip_dirs()
p.sort_stats('tottime').print_stats(10)
