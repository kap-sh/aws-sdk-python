"""Generated from Smithy shape ``com.amazonaws.ecs#LinearConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.double
    import aws_sdk_ecs.types.integer


class LinearConfiguration(TypedDict):
    step_percent: "aws_sdk_ecs.types.double.Double"
    """<p>The percentage of production traffic to shift in each step during a linear deployment. Valid values are multiples of 0.1 from 3.0 to 100.0. The default value is 10.0.</p>"""
    step_bake_time_in_minutes: "aws_sdk_ecs.types.integer.Integer"
    """<p>The amount of time in minutes to wait between each traffic shifting step during a linear deployment. Valid values are 0 to 1440 minutes (24 hours). The default value is 6. This bake time is not applied after reaching 100 percent traffic.</p>"""
