"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ListRecommendedActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_recommended_actions.types.max_results
    import capo_bcm_recommended_actions.types.next_token
    import capo_bcm_recommended_actions.types.request_filter


class ListRecommendedActionsRequest(TypedDict, closed=True):
    filter: NotRequired[
        "capo_bcm_recommended_actions.types.request_filter.RequestFilter"
    ]
    """<p>The criteria that you want all returned recommended actions to match.</p>"""
    max_results: NotRequired[
        "capo_bcm_recommended_actions.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_bcm_recommended_actions.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendedActionsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_bcm_recommended_actions.types.request_filter

        out["filter"] = (
            capo_bcm_recommended_actions.types.request_filter.serialize_aws_json_1_0(
                value["filter"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendedActionsRequest:
    out: ListRecommendedActionsRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import capo_bcm_recommended_actions.types.request_filter

        out["filter"] = (
            capo_bcm_recommended_actions.types.request_filter.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
