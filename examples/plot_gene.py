"""
Plot expression of a gene in all phenotypes
==========================================

In each column of the phenotype, the pooled samples are plotted as black dots
and the outliers are plotted as grey shadows.

"""
import flotilla
study = flotilla.embark(flotilla._brainspan)
study.plot_gene("FOXP1")