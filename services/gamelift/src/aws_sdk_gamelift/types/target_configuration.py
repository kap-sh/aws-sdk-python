"""Generated from Smithy shape ``com.amazonaws.gamelift#TargetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.double


class TargetConfiguration(TypedDict):
    target_value: NotRequired["aws_sdk_gamelift.types.double.Double"]
    """<p>Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetConfiguration) -> dict:
    out: dict = {}
    if "target_value" in value:
        out["TargetValue"] = value["target_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetConfiguration:
    out: TargetConfiguration = {}  # type: ignore[typeddict-item]
    if "TargetValue" in data:
        out["target_value"] = data["TargetValue"]
    return out
