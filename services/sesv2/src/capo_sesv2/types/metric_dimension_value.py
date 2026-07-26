"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricDimensionValue``."""

from typing import TypeAlias

"""<p>A list of values associated with the <code>MetricDimensionName</code> to filter metrics by. Can either be <code>*</code> as a wildcard for all values or a list of up to 10 specific values. If one <code>Dimension</code> has the <code>*</code> value, other dimensions can only contain one value. </p>"""
MetricDimensionValue: TypeAlias = str
