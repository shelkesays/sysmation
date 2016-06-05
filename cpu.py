f = open("/proc/cpuinfo")

cpuinfo = {}
for line in enumerate(f):
    info = str(line[1]).split(':')
    if len(info) > 1:
        index = str(info[0]).strip()
        data = str(info[1]).strip()
        if index in cpuinfo and cpuinfo[index] != data:
            if str(cpuinfo[index]).isdigit():
                cpuinfo[index] = int(cpuinfo[index]) + int(data)
            else:
                cpuinfo[index] = cpuinfo[index] + data
        else:
            cpuinfo[index] = data

for key, value in cpuinfo.iteritems():
    print "{}: {}".format(key, value)
