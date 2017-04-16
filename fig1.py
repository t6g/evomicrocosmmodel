from pylab import *

cnt   = loadtxt('data/control.txt')
et1   = loadtxt('data/et1.txt')
et2   = loadtxt('data/et2.txt')
ot1a  = loadtxt('data/ot1a.txt')
ot1b  = loadtxt('data/ot1b.txt')
ot2a  = loadtxt('data/ot2a.txt')
ot2b  = loadtxt('data/ot2b.txt')
ot3a  = loadtxt('data/ot3a.txt')
ot3b  = loadtxt('data/ot3b.txt')
ev1a  = loadtxt('data/ev1a.txt')
ev1b  = loadtxt('data/ev1b.txt')
ev2   = loadtxt('data/ev2.txt')
et1pa = loadtxt('0/et1.txt')
et1pb = loadtxt('1/et1.txt')
et2pa = loadtxt('0/et2.txt')
et2pb = loadtxt('1/et2.txt')
ot1pa = loadtxt('0/ot1.txt')
ot1pb = loadtxt('1/ot1.txt')
ot2pa = loadtxt('0/ot2.txt')
ot2pb = loadtxt('1/ot2.txt')
ot3pa = loadtxt('0/ot3.txt')
ot3pb = loadtxt('1/ot3.txt')
ev1pa = loadtxt('0/ev1.txt')
ev1pb = loadtxt('1/ev1.txt')
ev2pa = loadtxt('0/ev2.txt')
ev2pb = loadtxt('1/ev2.txt')

figure()

xmax  = 200.0
ymaxs = 10.0
ymaxa = 10.0
ymaxu = 50.0 

t = et1pa[:, 1]/86400.0
subplots_adjust(hspace=0.001, wspace=0.00001)

ax1=subplot(3, 3, 1);
plot(et1[:, 0], et1[:, 3]*1000.0, 'bo', et2[:, 0], et2[:, 3]*1000.0, 'r^', cnt[:, 0], cnt[:, 3], 'kd', t, et1pa[:, 9]*1e3, 'b--', t, et2pa[:, 9]*1e3, 'r--', t, et1pb[:, 9]*1e3, '-b', t, et2pb[:, 9]*1e3, '-r', linewidth=2)
l = legend(('+ 0.00 mM $\mathrm{SO_4^{2-}}$', '+ 3.85 mM $\mathrm{SO_4^{2-}}$', 'control'), numpoints=1)
l.draw_frame(False)
x = l.get_texts();
setp(x, fontsize='small');
xlim([0, xmax])
ylim([0, ymaxa])
ylabel('Acetate (mM)');
text(10, 9, '(a)')
text(75,10.5,'Ethanol')

text(-80,12,'Figure 1', fontsize='x-large', color='b')

ax4=subplot(3, 3, 4);
plot(et1[:, 0], et1[:, 4]*1000.0, 'bo', et2[:, 0], et2[:, 4]*1000.0, 'r^', cnt[:, 0], cnt[:, 4], 'kd', t, et1pa[:, 12]*1e3, 'b--', t, et2pa[:, 12]*1e3, 'r--', t, et1pb[:, 12]*1e3, 'b-', t, et2pb[:, 12]*1e3, 'r-', linewidth=2)
xlim([0, xmax])
ylim([0, ymaxs])
ylabel('Sulfate (mM)');
yticks([0, 2, 4, 6, 8])
text(10, 9, '(d)')

ax7=subplot(3, 3, 7);
plot(et1[:, 0], et1[:, 2]*1e6, 'bo', et2[:, 0], et2[:, 2]*1e6, 'r^', cnt[:, 0], cnt[:, 2]*1e3, 'kd', t, et1pa[:, 14]*1e6, 'b--', t, et2pa[:, 14]*1e6, 'r--', t, et1pb[:, 14]*1e6, '-b', t, et2pb[:, 14]*1e6, '-r', linewidth=2)
xlim([0, xmax])
ylim([0, ymaxu])
xlabel('Elapsed time (day)');
ylabel('U(VI) ($\mathrm{\mu}$M)');
text(10,ymaxu*0.9, '(g)')
yticks([0, 10, 20, 30, 40])
xticks([0, 50, 100, 150])

ax2=subplot(3, 3, 2);
ox  = ot1a[:, 0]
o1a = ot1a[:, 3]*1e3 
o1b = ot1b[:, 3]*1e3
o1  = 0.5 * (o1a + o1b)
o1a = abs(o1a - o1)
o1b = abs(o1b - o1)

o2a = ot2a[:, 3]*1e3 
o2b = ot2b[:, 3]*1e3
o2  = 0.5 * (o2a + o2b)
o2a = abs(o2a - o2)
o2b = abs(o2b - o2)

o3a = ot3a[:, 3]*1e3 
o3b = ot3b[:, 3]*1e3
o3  = 0.5 * (o3a + o3b)
o3a = abs(o3a - o3)
o3b = abs(o3b - o3)

errorbar(ox, o1, yerr=[o1a,o1b],fmt='ob') 
hold
errorbar(ox, o2, yerr=[o2a,o2b],fmt='sr') 
errorbar(ox, o3, yerr=[o3a,o3b],fmt='^g') 
plot(ot1pa[:, 9]*1e3, 'b--', t, ot2pa[:, 9]*1e3, 'r--', t, ot3pa[:, 9]*1e3, 'g--', t, ot1pb[:, 9]*1e3, 'b-', t, ot2pb[:, 9]*1e3, 'r-', t, ot3pb[:, 9]*1e3, 'g-', linewidth=2);
xlim([0, xmax])
ylim([0, ymaxa])
text(10, 9, '(b)')
text(75,10.5,'Oleate')

ax5=subplot(3, 3, 5);
o1a = ot1a[:, 4]*1e3 
o1b = ot1b[:, 4]*1e3
o1  = 0.5 * (o1a + o1b)
o1a = abs(o1a - o1)
o1b = abs(o1b - o1)

o2a = ot2a[:, 4]*1e3 
o2b = ot2b[:, 4]*1e3
o2  = 0.5 * (o2a + o2b)
o2a = abs(o2a - o2)
o2b = abs(o2b - o2)

o3a = ot3a[:, 4]*1e3 
o3b = ot3b[:, 4]*1e3
o3  = 0.5 * (o3a + o3b)
o3a = abs(o3a - o3)
o3b = abs(o3b - o3)

errorbar(ox, o1, yerr=[o1a,o1b],fmt='ob') 
hold
errorbar(ox, o2, yerr=[o2a,o2b],fmt='sr') 
errorbar(ox, o3, yerr=[o3a,o3b],fmt='^g') 
plot(t, ot1pa[:, 12]*1e3, 'b--', t, ot2pa[:, 12]*1e3, 'r--', t, ot3pa[:, 12]*1e3, 'g--', t, ot1pb[:, 12]*1e3, 'b-', t, ot2pb[:, 12]*1e3, 'r-', t, ot3pb[:, 12]*1e3, 'g-', linewidth=2);
l = legend(('+ 0.00 mM $\mathrm{SO_4^{2-}}$', '+ 3.85 mM $\mathrm{SO_4^{2-}}$', '+ 7.70 mM $\mathrm{SO_4^{2-}}$'), numpoints=1)
l.draw_frame(False)
x = l.get_texts();
setp(x, fontsize='small');
xlim([0, xmax])
ylim([0, ymaxs])
text(10, 9, '(e)')

ax8=subplot(3, 3, 8);
o1a = ot1a[:, 2]*1e6 
o1b = ot1b[:, 2]*1e6
o1  = 0.5 * (o1a + o1b)
o1a = abs(o1a - o1)
o1b = abs(o1b - o1)

o2a = ot2a[:, 2]*1e6 
o2b = ot2b[:, 2]*1e6
o2  = 0.5 * (o2a + o2b)
o2a = abs(o2a - o2)
o2b = abs(o2b - o2)

o3a = ot3a[:, 2]*1e6 
o3b = ot3b[:, 2]*1e6
o3  = 0.5 * (o3a + o3b)
o3a = abs(o3a - o3)
o3b = abs(o3b - o3)

errorbar(ox, o1, yerr=[o1a,o1b],fmt='ob') 
hold
errorbar(ox, o2, yerr=[o2a,o2b],fmt='sr') 
errorbar(ox, o3, yerr=[o3a,o3b],fmt='^g') 
plot(t, ot1pa[:, 14]*1e6, 'b--', t, ot2pa[:, 14]*1e6, 'r--', t, ot3pa[:, 14]*1e6, 'g--', t, ot1pb[:, 14]*1e6, 'b-', t, ot2pb[:, 14]*1e6, 'r-', t, ot3pb[:, 14]*1e6, 'g-', linewidth=2);
xlim([0, xmax])
ylim([0, ymaxu])
text(10, ymaxu*0.9, '(h)')
xlabel('Elapsed time (day)');
xticks([0, 50, 100, 150])

ax3=subplot(3, 3, 3);
ex  = ev1a[:, 0]
e1a = ev1a[:, 3]*1e3 
e1b = ev1b[:, 3]*1e3
e1  = 0.5 * (e1a + e1b)
e1a = abs(e1a - e1)
e1b = abs(e1b - e1)
errorbar(ex, e1, yerr=[e1a,e1b],fmt='ob') 
hold
plot(ev2[:, 0], ev2[:, 3]*1e3, 'r^', t, ev1pa[:, 9]*1e3, 'b--', t, ev2pa[:, 9]*1e3, 'r--', t, ev1pb[:, 9]*1e3, 'b-', t, ev2pb[:, 9]*1e3, 'r-', linewidth=2);
xlim([0, xmax])
ylim([0, ymaxa])
text(10, 9, '(c)')
text(90,10.5,'EVO')

ax6=subplot(3, 3, 6);
e1a = ev1a[:, 4]*1e3 
e1b = ev1b[:, 4]*1e3
e1  = 0.5 * (e1a + e1b)
e1a = abs(e1a - e1)
e1b = abs(e1b - e1)
errorbar(ex, e1, yerr=[e1a,e1b],fmt='ob') 
hold
plot(ev2[:, 0], ev2[:, 4]*1e3, 'r^', t, ev1pa[:, 12]*1e3, 'b--', t, ev2pa[:, 12]*1e3, 'r--', t, ev1pb[:, 12]*1e3, 'b-', t, ev2pb[:, 12]*1e3, 'r-', linewidth=2);
l = legend(('+ 0.00 mM $\mathrm{SO_4^{2-}}$', '+ 3.85 mM $\mathrm{SO_4^{2-}}$'),numpoints=1)
l.draw_frame(False)
x = l.get_texts();
setp(x, fontsize='small');
xlim([0, xmax])
ylim([0, ymaxs])
text(10, 9, '(f)')

ax9=subplot(3, 3, 9);
e1a = ev1a[:, 2]*1e6 
e1b = ev1b[:, 2]*1e6
e1  = 0.5 * (e1a + e1b)
e1a = abs(e1a - e1)
e1b = abs(e1b - e1)
plot(t, ev1pa[:, 14]*1e6, 'b--', t, ev1pb[:, 14]*1e6, 'b-', ev2[:, 0], ev2[:, 2]*1e6, 'r^', t, ev2pa[:, 14]*1e6, 'r--', t, ev2pb[:, 14]*1e6, 'r-', linewidth=2);
hold
errorbar(ex, e1, yerr=[e1a,e1b],fmt='ob') 
l = legend(('Model', 'Model w. lag time'),numpoints=1)
l.draw_frame(False)
x = l.get_texts();
setp(x, fontsize='small');
xlim([0, xmax])
ylim([0, ymaxu])
xlabel('Elapsed time (day)');
text(10, ymaxu*0.9, '(i)')

xticklabels=ax1.get_xticklabels()+ax2.get_xticklabels()+ax3.get_xticklabels()+ax4.get_xticklabels()+ax5.get_xticklabels()+ax6.get_xticklabels()
yticklabels=ax2.get_yticklabels()+ax3.get_yticklabels()+ax5.get_yticklabels()+ax6.get_yticklabels()+ax8.get_yticklabels()+ax9.get_yticklabels()
setp(xticklabels, visible=False)
setp(yticklabels, visible=False)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 7)
savefig('fig1.pdf')
show()
