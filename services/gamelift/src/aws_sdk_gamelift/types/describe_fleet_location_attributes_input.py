"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetLocationAttributesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.location_list
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.positive_integer


class DescribeFleetLocationAttributesInput(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to retrieve remote locations for. You can use either the fleet ID or ARN value.</p>"""
    locations: NotRequired["aws_sdk_gamelift.types.location_list.LocationList"]
    """<p>A list of fleet locations to retrieve information for. Specify locations in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>"""
    limit: NotRequired["aws_sdk_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This limit is not currently enforced.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetLocationAttributesInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "locations" in value:
        import aws_sdk_gamelift.types.location_list

        out["Locations"] = aws_sdk_gamelift.types.location_list.serialize_aws_json_1_1(
            value["locations"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetLocationAttributesInput:
    out: DescribeFleetLocationAttributesInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "Locations" in data:
        import aws_sdk_gamelift.types.location_list

        out["locations"] = (
            aws_sdk_gamelift.types.location_list.deserialize_aws_json_1_1(
                data["Locations"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
