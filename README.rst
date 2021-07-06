=======
rstdiff
=======

Overview
========

`rstdiff` takes two reStructuredText documents as input, does a
structural comaprison on them and produces an annotated result
highlighting the changes. `rstdiff` "understands" reStructuredText
and therefore is able to care for the subtleties of such a comparison
the result is usually much more useful than a plain source diff.

The result is then written by a Docutils writer. Use the `--writer`
option to select a writer for the result.

Installation
============

`rstdiff` uses the standard Distutils package. Thus the
installation is done with something like::

  python setup.py install


Usage
=====

SYNOPSIS
--------

**rstdiff.py** [*options*]... *old-reST* [*new-reST* [*diff-output*]]

DESCRIPTION
-----------

Generates a structural diff from two reStructuredText input documents
and produces an annotated result.

OPTIONS
-------

::

  --writer=WRITER         Select writer to write output with (default "xml").
  --old                   Following options apply to the old input document
                          (default: both input documents).
  --new                   Following options apply to the new input document
                          (default: both input documents).
  --both                  Following options apply to both input documents
                          (default).
  --compare-sections-by-names
                          Compare sections by comparing their names (default);
                          useful when section titles are stable but sections
                          change
  --compare-sections-normally
                          Compare sections normally; useful when section titles
                          change

SEE ALSO
========

Docutils
    http://docutils.sourceforge.net/

reStructuredText
    http://docutils.sourceforge.net/rst.html

Original Source
    https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/sandbox/rstdiff/

AVAILABILITY
============

**rstdiff** is available from

https://github.com/SamWilsn/rstdiff
