from pylab import *

ev1a  = loadtxt('data/ev1a.txt')
ev1b  = loadtxt('data/ev1b.txt')
ev1p = loadtxt('1/ev1toc.txt')

figure()

ex    = ev1a[:, 0]
ace1a = ev1a[:, 3]*1e3 
ace1b = ev1b[:, 3]*1e3
ace1  = 0.5 * (ace1a + ace1b)
ace1a = abs(ace1a - ace1)
ace1b = abs(ace1b - ace1)
errorbar(ex, ace1, yerr=[ace1a,ace1b],fmt='ob') 

hold
so41a = ev1a[:, 4]*1e3 
so41b = ev1b[:, 4]*1e3
so41  = 0.5 * (so41a + so41b)
so41a = abs(so41a - so41)
so41b = abs(so41b - so41)
errorbar(ex, so41, yerr=[so41a,so41b],fmt='sr') 

t = ev1p[:, 1]/86400.0
ax1 = subplot(111);
plot(t, ev1p[:, 6]*1e3, 'r-', t, ev1p[:, 5]*1e3, 'b-', linewidth=2);
xlim([0, 200])
ylim([0, 5])
xlabel('Time (day)');
ylabel('Sulfate/acetate (mM)');
annotate('$\mathrm{SO_4^{2-}}$', xy=(16, 1.2), xycoords='data', color='r');
annotate('$\mathrm{CH_3COO^-}$', xy=(80, 0.5), xycoords='data', color='b');
annotate('$\mathrm{U}$', xy=(4, 2.5), xycoords='data', color='m');
ax2 = twinx();
u6a1a = ev1a[:, 2]*1e6 
u6a1b = ev1b[:, 2]*1e6
u6a1  = 0.5 * (u6a1a + u6a1b)
u6a1a = abs(u6a1a - u6a1)
u6a1b = abs(u6a1b - u6a1)
errorbar(ex, u6a1, yerr=[u6a1a,u6a1b],fmt='dm') 
plot(t, ev1p[:, 7]*1e6, 'm-', linewidth=2);
xlim([0, 200])
ylim([0, 20])
ylabel('U ($\mu$M)');

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6, 4.3)
savefig('figtoc.png')
savefig('figtoc.pdf')
show()
