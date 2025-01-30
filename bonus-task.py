from mininet.topo import Topo

nodes = []
switches = []
links = []


class TutorialTopology(Topo):

    # --- Bonus Task ---
    def nodeCreate(self, nodeName):
        nodes.append(self.addHost(nodeName))

    def switchCreate(self, switchName):
        switches.append(self.addSwitch(switchName))

    # --- Bonus Task ---

    def build(self):

        # --- Bonus Task ---
        for i in range(10):
            self.nodeCreate('h' + str(i+1))

        for i in range(2):
            self.switchCreate('s' + str(i+1))

        for i in range(5):
            self.addLink(nodes[i], switches[0])
            self.addLink(nodes[i+5], switches[1])

        self.addLink(switches[0], switches[1])
        # --- Bonus Task ---


# the topologies accessible to the mn tool's `--topo` flag
# note: if using the Dockerfile, this must be the same as in the Dockerfile
topos = {'tutorialTopology': (lambda: TutorialTopology())}
