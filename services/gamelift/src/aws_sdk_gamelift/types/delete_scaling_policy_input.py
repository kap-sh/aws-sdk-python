"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteScalingPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.non_zero_and_max_string


class DeleteScalingPolicyInput(TypedDict):
    name: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.</p>"""
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to be deleted. You can use either the fleet ID or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteScalingPolicyInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteScalingPolicyInput:
    out: DeleteScalingPolicyInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    return out
