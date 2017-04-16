from pylab import *

pre1 = loadtxt('1/ev2.txt')
pre3 = loadtxt('1/evb.txt')

figure()

t        = pre1[:, 1] / 86400.0
acetate  = pre1[:, 9] * 1000.0
fe3      = pre1[:,19] * 1000.0
fe2      = pre1[:,20] * 1000.0
goethite = pre1[:,32] * 1000.0
fes      = pre1[:,34] * 1000.0
siderite = pre1[:,73] * 1000.0
sifera   = pre1[:,39];


aacetate  = pre3[:, 9] * 1000.0
afe3      = pre3[:,19] * 1000.0
afe2      = pre3[:,20] * 1000.0
agoethite = pre3[:,32] * 1000.0
afes      = pre3[:,34] * 1000.0
asiderite = pre3[:,73] * 1000.0
asifera   = pre3[:,39]

xmax = 200;

subplots_adjust(hspace=0.001)
ax1=subplot(2, 1, 1);
plot(t, sifera, 'b-', t, asifera, 'r--', linewidth=2)
l = legend(('Goethite', 'Ferrihydrite'))
l.draw_frame(False)
#x = l.get_texts();
#setp(x, fontsize='small');
xlim([0, xmax])
ylim([-100, 1000])
text(5, 890, '(a)')
ylabel('Growth index (FeRA)');
ax = gca()
for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize('xx-small')

subplot(2, 1, 2);
plot(t, goethite, 'b-', t, agoethite, 'r--', linewidth=2)
xlim([0, xmax])
ylim([0, 50])
ylabel('Concentration (mM)');
text(5, 45, '(b)')
xlabel('Elapsed time (day)');
ax = gca()
for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize('x-small')


text(-10,1100,'Figure 2', fontsize='x-large', color='b')

xticklabels=ax1.get_xticklabels()
setp(xticklabels, visible=False)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(4.5, 6)
savefig('fig2.pdf')
show()
