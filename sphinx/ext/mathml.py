from typing import TYPE_CHECKING

import sphinx


from docutils import nodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator


def html_visit_math(self: HTML5Translator, node: nodes.math) -> None:
    self.math_options = ""
    self.math_output = "mathml"
    self.super_visit_math(node)
    return


def html_visit_displaymath(self: HTML5Translator, node: nodes.math_block) -> None:
    self.math_options = ""
    self.math_output = "mathml"
    self.super_visit_math_block(node)
    return


def setup(app: Sphinx):
    app.add_html_math_renderer(
        'mathml',
        inline_renderers=(html_visit_math, None),
        block_renderers=(html_visit_displaymath, None),
    )

    return {
        'version': sphinx.__display_version__,
        'parallel_read_safe': True,
    }
