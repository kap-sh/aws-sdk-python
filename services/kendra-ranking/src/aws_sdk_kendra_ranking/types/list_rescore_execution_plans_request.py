"""Generated from Smithy shape ``com.amazonaws.kendraranking#ListRescoreExecutionPlansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request
    import aws_sdk_kendra_ranking.types.next_token


class ListRescoreExecutionPlansRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_kendra_ranking.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra Intelligent Ranking returns a pagination token in the response. You can use this pagination token to retrieve the next set of rescore execution plans.</p>"""
    max_results: NotRequired[
        "aws_sdk_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request.MaxResultsIntegerForListRescoreExecutionPlansRequest"
    ]
    """<p>The maximum number of rescore execution plans to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRescoreExecutionPlansRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRescoreExecutionPlansRequest:
    out: ListRescoreExecutionPlansRequest = {}  # type: ignore[typeddict-item]
    return out
