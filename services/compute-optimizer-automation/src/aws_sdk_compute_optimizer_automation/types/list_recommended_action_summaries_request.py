"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListRecommendedActionSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.next_token
    import aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list


class ListRecommendedActionSummariesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list.RecommendedActionFilterList"
    ]
    """<p>A list of filters to apply when retrieving recommended action summaries. Filters can be based on resource type, action type, account ID, and other criteria.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of recommended action summaries to return in a single response. Valid range is 1-1000.</p>"""
    next_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendedActionSummariesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list

        out["filters"] = (
            aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendedActionSummariesRequest:
    out: ListRecommendedActionSummariesRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list

        out["filters"] = (
            aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
