"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetAttributesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_attributes_list
    import aws_sdk_gamelift.types.non_zero_and_max_string


class DescribeFleetAttributesOutput(TypedDict):
    fleet_attributes: NotRequired[
        "aws_sdk_gamelift.types.fleet_attributes_list.FleetAttributesList"
    ]
    """<p>A collection of objects containing attribute metadata for each requested fleet ID. Attribute objects are returned only for fleets that currently exist.</p>"""
    next_token: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAttributesOutput) -> dict:
    out: dict = {}
    if "fleet_attributes" in value:
        import aws_sdk_gamelift.types.fleet_attributes_list

        out["FleetAttributes"] = (
            aws_sdk_gamelift.types.fleet_attributes_list.serialize_aws_json_1_1(
                value["fleet_attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAttributesOutput:
    out: DescribeFleetAttributesOutput = {}  # type: ignore[typeddict-item]
    if "FleetAttributes" in data:
        import aws_sdk_gamelift.types.fleet_attributes_list

        out["fleet_attributes"] = (
            aws_sdk_gamelift.types.fleet_attributes_list.deserialize_aws_json_1_1(
                data["FleetAttributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
