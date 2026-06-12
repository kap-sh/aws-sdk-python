"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetUtilizationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_utilization_list
    import aws_sdk_gamelift.types.non_zero_and_max_string


class DescribeFleetUtilizationOutput(TypedDict):
    fleet_utilization: NotRequired[
        "aws_sdk_gamelift.types.fleet_utilization_list.FleetUtilizationList"
    ]
    """<p>A collection of objects containing utilization information for each requested fleet ID. Utilization objects are returned only for fleets that currently exist.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetUtilizationOutput) -> dict:
    out: dict = {}
    if "fleet_utilization" in value:
        import aws_sdk_gamelift.types.fleet_utilization_list

        out["FleetUtilization"] = (
            aws_sdk_gamelift.types.fleet_utilization_list.serialize_aws_json_1_1(
                value["fleet_utilization"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetUtilizationOutput:
    out: DescribeFleetUtilizationOutput = {}  # type: ignore[typeddict-item]
    if "FleetUtilization" in data:
        import aws_sdk_gamelift.types.fleet_utilization_list

        out["fleet_utilization"] = (
            aws_sdk_gamelift.types.fleet_utilization_list.deserialize_aws_json_1_1(
                data["FleetUtilization"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
