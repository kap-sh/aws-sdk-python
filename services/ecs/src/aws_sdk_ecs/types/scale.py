"""Generated from Smithy shape ``com.amazonaws.ecs#Scale``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.double
    import aws_sdk_ecs.types.scale_unit


class Scale(TypedDict):
    value: "aws_sdk_ecs.types.double.Double"
    """<p>The value, specified as a percent total of a service's <code>desiredCount</code>, to scale the task set. Accepted values are numbers between 0 and 100.</p>"""
    unit: NotRequired["aws_sdk_ecs.types.scale_unit.ScaleUnit"]
    """<p>The unit of measure for the scale value.</p>"""
