from pylab import *

ev1p = loadtxt('1/ev1.txt')
ev2p = loadtxt('1/ev2.txt')

figure()

xmax = 200.0
ymax = 0.2

t = ev1p[:, 1]/86400.0

subplots_adjust(hspace=0.001, wspace=0.00001)
ax1=subplot(2, 3, 1);
plot(t, ev1p[:, 65]*1e3, 'b-', t, ev1p[:, 59]*1e3, 'r--', t, ev1p[:, 67]*1e3, 'g-.', linewidth=2)
xlim([0, xmax])
ylim([0, ymax])
ylabel('$\mathrm{C_5H_7O_2N}$ (mM)');
text(10, 0.85*ymax, '(a) + 0 mM S$\mathrm{O_4^{2-}}$')
l = legend(('Fermentors', 'Fe reducers', 'Acetogens'), loc='center left')
l.draw_frame(False)
x = l.get_texts();
setp(x, fontsize='medium');
text(-50, 0.22,'Figure 4', fontsize='x-large', color='b')

ax2=subplot(2, 3, 2);
plot(t, ev1p[:, 55]*1e3, 'b-', t, ev1p[:, 53]*1e3, 'r--', t, ev1p[:, 57]*1e3, 'g-.', linewidth=2)
xlim([0, xmax])
ylim([0, ymax])
#text(50, 1.1*ymax, 'Sulfate reducers')
text(10, 0.85*ymax, '(b) + 0 mM S$\mathrm{O_4^{2-}}$')
l = legend(('Acetate-utilizing SRB', '$\mathrm{H_2}$-utilizing SRB', 'LCFA-utilizing SRB'), loc='center left')
l.draw_frame(False)
x = l.get_texts();
setp(x, fontsize='medium');

ax3=subplot(2, 3, 3);
plot(t, ev1p[:, 69]*1e3, 'b-', t, ev1p[:, 71]*1e3, 'r--', linewidth=2)
xlim([0, xmax])
ylim([0, ymax])
text(10, 0.85*ymax, '(c) + 0 mM S$\mathrm{O_4^{2-}}$')
#text(45, 1.1*ymax, 'Methanogens')
l = legend(('Acetate-utilizing methanogen', '$\mathrm{H_2}$-utilizing methanogen'), loc='center left')
l.draw_frame(False)
x = l.get_texts();
setp(x, fontsize='medium');

ax4=subplot(2, 3, 4);
plot(t, ev2p[:, 65]*1e3, 'b-', t, ev2p[:, 59]*1e3, 'r--', t, ev2p[:, 67]*1e3, 'g-.', linewidth=2)
xlim([0, xmax])
ylim([0, ymax])
ylabel('$\mathrm{C_5H_7O_2N}$ (mM)');
text(10, 0.85*ymax, '(d) + 3.85 mM S$\mathrm{O_4^{2-}}$')
xlabel('Elapsed time (day)');
xticks([0, 50, 100, 150])
yticks([0, 0.05, 0.1, 0.15])

ax5=subplot(2, 3, 5);
plot(t, ev2p[:, 55]*1e3, 'b-', t, ev2p[:, 53]*1e3, 'r--', t, ev2p[:, 57]*1e3, 'g-.', linewidth=2)
xlim([0, xmax])
ylim([0, ymax])
text(10, 0.85*ymax, '(e) + 3.85 mM S$\mathrm{O_4^{2-}}$')
setp(x, fontsize='medium');
xlabel('Elapsed time (day)');
xticks([0, 50, 100, 150])

ax6=subplot(2, 3, 6);
plot(t, ev2p[:, 69]*1e3, 'b-', t, ev2p[:, 71]*1e3, 'r--', linewidth=2)
xlim([0, xmax])
ylim([0, ymax])
text(10, 0.85*ymax, '(f) + 3.85 mM S$\mathrm{O_4^{2-}}$')
xlabel('Elapsed time (day)');

xticklabels=ax1.get_xticklabels() + ax2.get_xticklabels() + ax3.get_xticklabels()
yticklabels=ax2.get_yticklabels() + ax3.get_yticklabels() + ax5.get_yticklabels() + ax6.get_yticklabels()
setp(xticklabels, visible=False)
setp(yticklabels, visible=False)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 6.5)
savefig('fig4.pdf')
show()
