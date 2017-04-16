from pylab import *

ot1a  = loadtxt('data/ot1a.txt')
ot1b  = loadtxt('data/ot1b.txt')
ot2a  = loadtxt('data/ot2a.txt')
ot2b  = loadtxt('data/ot2b.txt')
ot3a  = loadtxt('data/ot3a.txt')
ot3b  = loadtxt('data/ot3b.txt')
ev1a  = loadtxt('data/ev1a.txt')
ev1b  = loadtxt('data/ev1b.txt')
ev2   = loadtxt('data/ev2.txt')
ev1pa = loadtxt('1/ev10.txt')
ev1pb = loadtxt('1/ev1.txt')
ev1pc = loadtxt('1/ev11.txt')
ev2pa = loadtxt('1/ev20.txt')
ev2pb = loadtxt('1/ev2.txt')
ev2pc = loadtxt('1/ev21.txt')

figure()

xmax  = 200.0
ymaxs = 6.0
ymaxa = 6.0
ymaxu = 50.0 

t = ev1pa[:, 1]/86400.0

subplots_adjust(hspace=0.001)
ax1=subplot(3, 1, 1);
ex  = ev1a[:, 0]
e1a = ev1a[:, 3]*1e3 
e1b = ev1b[:, 3]*1e3
e1  = 0.5 * (e1a + e1b)
e1a = abs(e1a - e1)
e1b = abs(e1b - e1)
errorbar(ex, e1, yerr=[e1a,e1b],fmt='ob') 
hold
plot(ev2[:, 0], ev2[:, 3]*1e3, 'r^', t, ev1pa[:, 9]*1e3, 'b-.', t, ev2pa[:, 9]*1e3, 'r-.', t, ev1pb[:, 9]*1e3, 'b-', t, ev2pb[:, 9]*1e3, 'r-', t, ev1pc[:, 9]*1e3, '--b', t, ev2pc[:, 9]*1e3, '--r', linewidth=2)
xlim([0, xmax])
ylim([0, ymaxa])
text(175, 5.4, '(a)')
ylabel('Acetate (mM)');
text(-10,7,'Figure 3', fontsize='x-large', color='b')

ax2=subplot(3, 1, 2);
e1a = ev1a[:, 4]*1e3 
e1b = ev1b[:, 4]*1e3
e1  = 0.5 * (e1a + e1b)
e1a = abs(e1a - e1)
e1b = abs(e1b - e1)
errorbar(ex, e1, yerr=[e1a,e1b],fmt='ob') 
hold
plot(ev2[:, 0], ev2[:, 4]*1e3, 'r^', t, ev1pa[:, 12]*1e3, 'b-.', t, ev2pa[:, 12]*1e3, 'r-.', t, ev1pb[:, 12]*1e3, 'b-', t, ev2pb[:, 12]*1e3, 'r-', t, ev1pc[:, 12]*1e3, 'b--', t, ev2pc[:, 12]*1e3, 'r--', linewidth=2)
l = legend(('+ 0.00 mM $\mathrm{SO_4^{2-}}$', '+ 3.85 mM $\mathrm{SO_4^{2-}}$'),numpoints=1,loc=7)
l.draw_frame(False)
#x = l.get_texts();
#setp(x, fontsize='small');
xlim([0, xmax])
ylim([0, ymaxs])
text(175, 5.4, '(b)')
ylabel('Sulfate (mM)');
yticks([0, 1, 2, 3, 4, 5])

ax3=subplot(3, 1, 3);
e1a = ev1a[:, 2]*1e6 
e1b = ev1b[:, 2]*1e6
e1  = 0.5 * (e1a + e1b)
e1a = abs(e1a - e1)
e1b = abs(e1b - e1)
plot(t, ev1pa[:, 14]*1e6, 'b-.', t, ev1pb[:, 14]*1e6, 'b-', t, ev1pc[:, 14]*1e6, 'b--', ev2[:, 0], ev2[:, 2]*1e6, 'r^', t, ev2pa[:, 14]*1e6, 'r-.', t, ev2pb[:, 14]*1e6, 'r-', t, ev2pc[:, 14]*1e6, 'r--', linewidth=2)
hold
errorbar(ex, e1, yerr=[e1a,e1b],fmt='ob') 
l = legend(('$\mathrm{k_{h} = 1 x 10^{-5} M^{-1}s^{-1}}$', '$\mathrm{k_{h} = 3 x 10^{-5} M^{-1}s^{-1}} $', '$\mathrm{k_{h} = 3 x 10^{-4} M^{-1}s^{-1}} $'),loc=7);
l.draw_frame(False)
#x = l.get_texts();
#setp(x, fontsize='small');
xlim([0, xmax])
ylim([0, ymaxu])
xlabel('Elapsed time (day)');
text(175, ymaxu*0.9, '(c)')
ylabel('U(VI) ($\mathrm{\mu}$M)');
yticks([0, 10, 20, 30, 40])

xticklabels=ax1.get_xticklabels() + ax2.get_xticklabels()
setp(xticklabels, visible=False)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4.5, 8)
savefig('fig3.pdf')
show()
