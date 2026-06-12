"""Generated from Smithy shape ``com.amazonaws.connect#SearchEvaluationFormsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.evaluation_form_search_summary_list
    import aws_sdk_connect.types.next_token


class SearchEvaluationFormsResponse(TypedDict):
    evaluation_form_search_summary_list: NotRequired[
        "aws_sdk_connect.types.evaluation_form_search_summary_list.EvaluationFormSearchSummaryList"
    ]
    """<p>Information about the returned evaluation forms.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of evaluation forms that matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchEvaluationFormsResponse) -> dict:
    out: dict = {}
    if "evaluation_form_search_summary_list" in value:
        import aws_sdk_connect.types.evaluation_form_search_summary_list

        out["EvaluationFormSearchSummaryList"] = (
            aws_sdk_connect.types.evaluation_form_search_summary_list.serialize_json(
                value["evaluation_form_search_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchEvaluationFormsResponse:
    out: SearchEvaluationFormsResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationFormSearchSummaryList" in data:
        import aws_sdk_connect.types.evaluation_form_search_summary_list

        out["evaluation_form_search_summary_list"] = (
            aws_sdk_connect.types.evaluation_form_search_summary_list.deserialize_json(
                data["EvaluationFormSearchSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
