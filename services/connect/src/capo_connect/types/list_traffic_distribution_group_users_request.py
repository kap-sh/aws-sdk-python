"""Generated from Smithy shape ``com.amazonaws.connect#ListTrafficDistributionGroupUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.max_result10
    import capo_connect.types.next_token
    import capo_connect.types.traffic_distribution_group_id_or_arn


class ListTrafficDistributionGroupUsersRequest(TypedDict, closed=True):
    traffic_distribution_group_id: "capo_connect.types.traffic_distribution_group_id_or_arn.TrafficDistributionGroupIdOrArn"
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.</p>"""
    max_results: NotRequired["capo_connect.types.max_result10.MaxResult10"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrafficDistributionGroupUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTrafficDistributionGroupUsersRequest:
    out: ListTrafficDistributionGroupUsersRequest = {}  # type: ignore[typeddict-item]
    return out
