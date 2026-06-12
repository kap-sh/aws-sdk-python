"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ListRecommendedActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_recommended_actions.types.max_results
    import aws_sdk_bcm_recommended_actions.types.next_token
    import aws_sdk_bcm_recommended_actions.types.request_filter


class ListRecommendedActionsRequest(TypedDict):
    filter: NotRequired[
        "aws_sdk_bcm_recommended_actions.types.request_filter.RequestFilter"
    ]
    """<p>The criteria that you want all returned recommended actions to match.</p>"""
    max_results: NotRequired[
        "aws_sdk_bcm_recommended_actions.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_recommended_actions.types.next_token.NextToken"
    ]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendedActionsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_bcm_recommended_actions.types.request_filter

        out["filter"] = (
            aws_sdk_bcm_recommended_actions.types.request_filter.serialize_aws_json_1_0(
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
        import aws_sdk_bcm_recommended_actions.types.request_filter

        out["filter"] = (
            aws_sdk_bcm_recommended_actions.types.request_filter.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
