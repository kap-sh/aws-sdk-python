"""Generated from Smithy shape ``com.amazonaws.gamelift#TargetTrackingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_negative_double


class TargetTrackingConfiguration(TypedDict):
    target_value: NotRequired[
        "aws_sdk_gamelift.types.non_negative_double.NonNegativeDouble"
    ]
    """<p>Desired value to use with a game server group target-based scaling policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingConfiguration) -> dict:
    out: dict = {}
    if "target_value" in value:
        out["TargetValue"] = value["target_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingConfiguration:
    out: TargetTrackingConfiguration = {}  # type: ignore[typeddict-item]
    if "TargetValue" in data:
        out["target_value"] = data["TargetValue"]
    return out
