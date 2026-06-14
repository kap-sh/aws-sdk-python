"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetLocationAttributesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_arn
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.location_attributes_list
    import aws_sdk_gamelift.types.non_zero_and_max_string


class DescribeFleetLocationAttributesOutput(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that location attributes were requested for.</p>"""
    fleet_arn: NotRequired["aws_sdk_gamelift.types.fleet_arn.FleetArn"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    location_attributes: NotRequired[
        "aws_sdk_gamelift.types.location_attributes_list.LocationAttributesList"
    ]
    """<p> Location-specific information on the requested fleet's remote locations.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetLocationAttributesOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "location_attributes" in value:
        import aws_sdk_gamelift.types.location_attributes_list

        out["LocationAttributes"] = (
            aws_sdk_gamelift.types.location_attributes_list.serialize_aws_json_1_1(
                value["location_attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetLocationAttributesOutput:
    out: DescribeFleetLocationAttributesOutput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "FleetArn" in data:
        out["fleet_arn"] = data["FleetArn"]
    if "LocationAttributes" in data:
        import aws_sdk_gamelift.types.location_attributes_list

        out["location_attributes"] = (
            aws_sdk_gamelift.types.location_attributes_list.deserialize_aws_json_1_1(
                data["LocationAttributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
