"""Generated from Smithy shape ``com.amazonaws.ecs#CanaryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.double
    import aws_sdk_ecs.types.integer


class CanaryConfiguration(TypedDict, closed=True):
    canary_percent: NotRequired["aws_sdk_ecs.types.double.Double"]
    """<p>The percentage of production traffic to shift to the new service revision during the canary phase. Valid values are multiples of 0.1 from 0.1 to 100.0. The default value is 5.0.</p>"""
    canary_bake_time_in_minutes: NotRequired["aws_sdk_ecs.types.integer.Integer"]
    """<p>The amount of time in minutes to wait during the canary phase before shifting the remaining production traffic to the new service revision. Valid values are 0 to 1440 minutes (24 hours). The default value is 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CanaryConfiguration) -> dict:
    out: dict = {}
    if "canary_percent" in value:
        out["canaryPercent"] = value["canary_percent"]
    if "canary_bake_time_in_minutes" in value:
        out["canaryBakeTimeInMinutes"] = value["canary_bake_time_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CanaryConfiguration:
    out: CanaryConfiguration = {}  # type: ignore[typeddict-item]
    if "canaryPercent" in data:
        out["canary_percent"] = data["canaryPercent"]
    if "canaryBakeTimeInMinutes" in data:
        out["canary_bake_time_in_minutes"] = data["canaryBakeTimeInMinutes"]
    return out
