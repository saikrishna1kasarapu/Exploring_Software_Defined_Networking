
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        hosth1 = self.addHost( 'h1' )
        hosth2 = self.addHost( 'h2' )
        switchs1 = self.addSwitch( 's1' )
        hosth3 = self.addHost('h3')
        hosth4 = self.addHost ( 'h4')
        switchs2 = self.addSwitch('s2')
        hosth5 = self.addHost('h5')
        hosth6 = self.addHost('h6')
        switchs3 = self.addSwitch('s3')
        hosth7 = self.addHost('h7')
        hosth8 = self.addHost('h8')
        switchs4 = self.addSwitch('s4')
        switchs5 = self.addSwitch('s5')
        switchs6 = self.addSwitch('s6')
        switchs7 = self.addSwitch('s7')
        # Add links
        self.addLink( hosth1, switchs1 )
        self.addLink( switchs1, hosth2 )
        self.addLink( switchs1, switchs5 )
        self.addLink( switchs5, switchs2 )
        self.addLink( switchs2, hosth3 )
        self.addLink( switchs2, hosth4 )
        self.addLink( switchs5, switchs7 )
        self.addLink( switchs7, switchs6 )
        self.addLink( switchs6, switchs3 )
        self.addLink( switchs3, hosth5 )
        self.addLink( switchs3, hosth6 )
        self.addLink( switchs6, switchs4 )
        self.addLink( switchs4, hosth7 )
        self.addLink(switchs4, hosth8 )


topos = { 'mytopo': ( lambda: MyTopo() ) }