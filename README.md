# Network Flow Fingerprint Recognizer
This tool models network traffic into to a [Formal Language](https://en.wikipedia.org/wiki/Formal_language) to find a generic grammar among the flows of encrypted traffic from/to a specific application.

## What exactly does this tool do?
Most of the data transferring on the network are encrypted, hence, it seems that there is no possible way to detect which application is running on the clients' device. So, instead of trying to decrypt packets streaming, we decided to find some patterns (e.g. IP, port, timing intervals, packet size, etc.) among these packets that come and go from/to each application. Using this technique, we teach these patterns to another tool (Which would be published on Github soon) to detect apps running on devices.

## To Do

- [x] Read packet flows from Pcap files
    -  [x] Test
- [x] Read and write packet flows from/to binary files
- [x] Split main into test/train data
    -  [ ] Test
- [ ] Split flows into batches
    -  [ ] Test
- [x] Load and save symbols
    -  [ ] Test
- [x] Finding symbols Strategies
    - [x] Sequence Recognizer
        -  [ ] Test

## Note
This app is currently under development
