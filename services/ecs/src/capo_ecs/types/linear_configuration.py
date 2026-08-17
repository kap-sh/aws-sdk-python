"""Generated from Smithy shape ``com.amazonaws.ecs#LinearConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.double
    import capo_ecs.types.integer


class LinearConfiguration(TypedDict, closed=True):
    step_percent: NotRequired["capo_ecs.types.double.Double"]
    """<p>The percentage of production traffic to shift in each step during a linear deployment. Valid values are multiples of 0.1 from 3.0 to 100.0. The default value is 10.0.</p>"""
    step_bake_time_in_minutes: NotRequired["capo_ecs.types.integer.Integer"]
    """<p>The amount of time in minutes to wait between each traffic shifting step during a linear deployment. Valid values are 0 to 1440 minutes (24 hours). The default value is 6. This bake time is not applied after reaching 100 percent traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LinearConfiguration) -> dict:
    out: dict = {}
    if "step_percent" in value:
        out["stepPercent"] = value["step_percent"]
    if "step_bake_time_in_minutes" in value:
        out["stepBakeTimeInMinutes"] = value["step_bake_time_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LinearConfiguration:
    out: LinearConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("stepPercent") is not None:
        out["step_percent"] = data["stepPercent"]
    if data.get("stepBakeTimeInMinutes") is not None:
        out["step_bake_time_in_minutes"] = data["stepBakeTimeInMinutes"]
    return out
