#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel



class MyNet( Topo ):
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )

    # Add switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )

        # Add links
        self.addLink( h1, s1 ,bw=10)
        self.addLink( h1, s2 ,bw=10)

        self.addLink( h2, s2 ,bw=10)
        self.addLink( h2, s3 ,bw=10)

        self.addLink( h3, s3 ,bw=10)

        self.addLink( s1, s2 ,bw=10)
        self.addLink( s1, s4 ,bw=10)

        self.addLink( s2, s3 ,bw=10)
        self.addLink( s2, s4 ,bw=10)
        self.addLink( s2, s5 ,bw=10)

        self.addLink( s3, s5 ,bw=10)

        self.addLink( s4, s5 ,bw=10)

        #adding controller

        floodlight = net.addController(name='floodlight' ,
                                 controller=RemoteController ,
                                 ip='192.168.56.101',
                                 port=6653)


if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    topo = MyNet()
    net = Mininet(topo)
    net.start()


#topos = { 'MyNet': ( lambda: MyNet() ) }
