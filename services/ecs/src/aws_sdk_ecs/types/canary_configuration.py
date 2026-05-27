"""Generated from Smithy shape ``com.amazonaws.ecs#CanaryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.double
    import aws_sdk_ecs.types.integer


class CanaryConfiguration(TypedDict):
    canary_percent: "aws_sdk_ecs.types.double.Double"
    """<p>The percentage of production traffic to shift to the new service revision during the canary phase. Valid values are multiples of 0.1 from 0.1 to 100.0. The default value is 5.0.</p>"""
    canary_bake_time_in_minutes: "aws_sdk_ecs.types.integer.Integer"
    """<p>The amount of time in minutes to wait during the canary phase before shifting the remaining production traffic to the new service revision. Valid values are 0 to 1440 minutes (24 hours). The default value is 10.</p>"""
