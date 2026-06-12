"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetPortSettingsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.location_string_model


class DescribeFleetPortSettingsInput(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to retrieve port settings for. You can use either the fleet ID or ARN value.</p>"""
    location: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>A remote location to check for status of port setting updates. Use the Amazon Web Services Region code format, such as <code>us-west-2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetPortSettingsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetPortSettingsInput:
    out: DescribeFleetPortSettingsInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "Location" in data:
        out["location"] = data["Location"]
    return out
