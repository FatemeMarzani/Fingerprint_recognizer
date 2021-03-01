# Network Flow Fingerprint Recognizer
This tool models network traffic into to a [Formal Language](https://en.wikipedia.org/wiki/Formal_language) to find a generic grammar among the flows of encrypted traffic from/to a specific application.

## What exactly this tool does?
Most of the data transferring on the network are encrypted, hence, it seems that there is no possible way to detect which application is running on the clients' device. So, instead of trying to decrypt packets streaming, we decided to find some patterns (e.g. IP, port, timing intervals, packet size, etc.) among these packets that come and go from/to each application. Using this technique, we teach these patterns to another tool (Which would be published on Github soon) to detect apps running on devices.

## To Do

- [x] Read packet flows from Pcap files
    -  [x] Test
- [x] Read and write packet flows from/to binary files
    -  [ ] Test
- [ ] Split flows into batches
    -  [ ] Test
- [ ] Load and save symbols
    -  [ ] Test
- [ ] Finding symbols
    -  [ ] Generate cluster of network destinations
    -  [ ] Generate cluster of network destinations

## Note
This app is currently under development