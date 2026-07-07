"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeRuntimeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_id_or_arn


class DescribeRuntimeConfigurationInput(TypedDict, closed=True):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to get the runtime configuration for. You can use either the fleet ID or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRuntimeConfigurationInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRuntimeConfigurationInput:
    out: DescribeRuntimeConfigurationInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    return out
