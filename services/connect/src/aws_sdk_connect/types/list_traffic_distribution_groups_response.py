"""Generated from Smithy shape ``com.amazonaws.connect#ListTrafficDistributionGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.traffic_distribution_group_summary_list


class ListTrafficDistributionGroupsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    traffic_distribution_group_summary_list: NotRequired[
        "aws_sdk_connect.types.traffic_distribution_group_summary_list.TrafficDistributionGroupSummaryList"
    ]
    """<p>A list of traffic distribution groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrafficDistributionGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "traffic_distribution_group_summary_list" in value:
        import aws_sdk_connect.types.traffic_distribution_group_summary_list

        out["TrafficDistributionGroupSummaryList"] = (
            aws_sdk_connect.types.traffic_distribution_group_summary_list.serialize_json(
                value["traffic_distribution_group_summary_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTrafficDistributionGroupsResponse:
    out: ListTrafficDistributionGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TrafficDistributionGroupSummaryList" in data:
        import aws_sdk_connect.types.traffic_distribution_group_summary_list

        out["traffic_distribution_group_summary_list"] = (
            aws_sdk_connect.types.traffic_distribution_group_summary_list.deserialize_json(
                data["TrafficDistributionGroupSummaryList"]
            )
        )
    return out
