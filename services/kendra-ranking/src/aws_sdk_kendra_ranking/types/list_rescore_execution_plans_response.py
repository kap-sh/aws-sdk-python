"""Generated from Smithy shape ``com.amazonaws.kendraranking#ListRescoreExecutionPlansResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.next_token
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_summary_list


class ListRescoreExecutionPlansResponse(TypedDict):
    summary_items: NotRequired[
        "aws_sdk_kendra_ranking.types.rescore_execution_plan_summary_list.RescoreExecutionPlanSummaryList"
    ]
    """<p>An array of summary information for one or more rescore execution plans.</p>"""
    next_token: NotRequired["aws_sdk_kendra_ranking.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra Intelligent Ranking returns a pagination token in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRescoreExecutionPlansResponse) -> dict:
    out: dict = {}
    if "summary_items" in value:
        import aws_sdk_kendra_ranking.types.rescore_execution_plan_summary_list

        out["SummaryItems"] = (
            aws_sdk_kendra_ranking.types.rescore_execution_plan_summary_list.serialize_aws_json_1_0(
                value["summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRescoreExecutionPlansResponse:
    out: ListRescoreExecutionPlansResponse = {}  # type: ignore[typeddict-item]
    if "SummaryItems" in data:
        import aws_sdk_kendra_ranking.types.rescore_execution_plan_summary_list

        out["summary_items"] = (
            aws_sdk_kendra_ranking.types.rescore_execution_plan_summary_list.deserialize_aws_json_1_0(
                data["SummaryItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
