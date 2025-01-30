from mininet.topo import Topo

nodes = []
switches = []
links = []


class TutorialTopology(Topo):

    # --- Task 3 ---
    def nodeCreate(self, nodeName):
        nodes.append(self.addHost(nodeName))

    def switchCreate(self, switchName):
        switches.append(self.addSwitch(switchName))

    # --- Task 3 ---

    def build(self):

        # --- Task 3 ---
        for i in range(10):
            self.nodeCreate('h' + str(i+1))

        for i in range(2):
            self.switchCreate('s' + str(i+1))

        for i in range(5):
            self.addLink(nodes[i], switches[0])
            self.addLink(nodes[i+5], switches[1])

        self.addLink(switches[0], switches[1], bw=50, delay='30ms', loss=10)
        # --- Task 3 ---


# the topologies accessible to the mn tool's `--topo` flag
# note: if using the Dockerfile, this must be the same as in the Dockerfile
topos = {'tutorialTopology': (lambda: TutorialTopology())}
