import platform

print("Architecture                   :", platform.architecture())
print("Processor                      :", platform.processor())
print("Machine                        :", platform.machine())
print("Node                           :", platform.node())
print("Platform                       :", platform.platform())
print("Platform with aliased          :", platform.platform(aliased=True))
print("Platform with terse            :", platform.platform(terse=True))
print("Platform with aliased and terse:", platform.platform(aliased=True, terse=True))
print("Release                        :", platform.release())
print("System                         :", platform.system())
print("Version                        :", platform.version())
print("Uname                          :", platform.uname())

print("Linux destribution             :", platform.linux_distribution())
print("Lib c version                  :", platform.libc_ver())
