"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetUtilizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn_list
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer


class DescribeFleetUtilizationInput(TypedDict, closed=True):
    fleet_ids: NotRequired["capo_gamelift.types.fleet_id_or_arn_list.FleetIdOrArnList"]
    """<p>A unique identifier for the fleet to retrieve utilization data for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter. </p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetUtilizationInput) -> dict:
    out: dict = {}
    if "fleet_ids" in value:
        import capo_gamelift.types.fleet_id_or_arn_list

        out["FleetIds"] = (
            capo_gamelift.types.fleet_id_or_arn_list.serialize_aws_json_1_1(
                value["fleet_ids"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetUtilizationInput:
    out: DescribeFleetUtilizationInput = {}  # type: ignore[typeddict-item]
    if "FleetIds" in data:
        import capo_gamelift.types.fleet_id_or_arn_list

        out["fleet_ids"] = (
            capo_gamelift.types.fleet_id_or_arn_list.deserialize_aws_json_1_1(
                data["FleetIds"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
