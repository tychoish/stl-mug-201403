SPHINXBUILD = sphinx-build
BUILDDIR = build

SPHINXOPTS = -q -c ./ $(PAPEROPT_$(PAPER))
SLIDESPHINXOPTS = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) source

.DEFAULT_GOAL:slides

$(BUILDDIR)/slides:slides
$(BUILDDIR)/html:html

.PHONY:stage

$(BUILDDIR)/output:$(BUILDDIR)/slides $(BUILDDIR)/html
	mkdir -p $@
	cp -R $(BUILDDIR)/html/* $@
	cp -R $(BUILDDIR)/slides $@

stage:$(BUILDDIR)/output

push:stage
	rsync -arz $(BUILDDIR)/output/ tychoish@foucault.cyborginstitute.net:/home/tychoish/public/tychoweb/stl-mug-201403

########################################################################

slides:
	$(SPHINXBUILD) -b slides $(SLIDESPHINXOPTS) $(BUILDDIR)/slides
	@echo "[SLIDES] HTML slide build complete."

html:
	$(SPHINXBUILD) -b html $(SLIDESPHINXOPTS) $(BUILDDIR)/html
	@echo "[HTML] site build complete."

clean:
	rm -rf $(BUILDDIR)
