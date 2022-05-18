# TCP Socket in GNS3

<!-- Put the link to this slide here so people can follow -->
slide: https://hackmd.io/p/template-Talk-slide

---

GNS3 allows the use of Docker files that enable the virualization of different components (StoneWork, Open vSwitch or Ubuntu-Docker-Guest).

In order to test network connectivity and simulate data traffic, the source files will be executed in two Ubuntu-Docker-Guest nodes, in order to observe the data transmission between client-server (in this case, UE-server).
 

---

## Project Folders

- :file_folder: tcpsocket-gns3 
    - Main folder with source code files for server and client, (Python 2.7)

---



### Usage flow

---


```graphviz
digraph {
  compound=true
  rankdir=RL

  graph [ fontname="Source Sans Pro", fontsize=20 ];
  node [ fontname="Source Sans Pro", fontsize=18];
  edge [ fontname="Source Sans Pro", fontsize=12 ];


  subgraph core {
    c [label="Beacon (4.2 or 5.0)"] [shape=box]
  }
  
  c -> a [ltail=session lhead=session]

  subgraph cluster1 {
     concentrate=true
    a [label="Data\nIPv6, TCP, MQTT (QoS 0)"] [shape=box]
   
    sync [label="port:(1883-21883)" shape=plaintext ]
    b -> sync  [dir="down"]
    sync -> a [dir="right"]
    label="Scanner (BLE 4.2)"
  }

  subgraph cluster2 {
    
    b [label="MongoDB"] [shape=box]
    sync [label="port:(1883-21883)" shape=plaintext ]
    label="Database"
  }
  
}
```
---
## Software Requirements

- GNS3
- VirtualBox
- GNS3_VM
- Ubuntu-Docker-Guest
---


## Required libraries



### Python (2.7.18)

```typescript
import socket
```

<br>

---

### Wrap up

- Cross envornment commnication
- A small library to solve messaging pain


---

### Thank you! :heart: 

You can find me on

- GitHub
