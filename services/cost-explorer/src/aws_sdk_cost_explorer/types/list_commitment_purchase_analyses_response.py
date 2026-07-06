"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCommitmentPurchaseAnalysesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.analysis_summary_list
    import aws_sdk_cost_explorer.types.next_page_token


class ListCommitmentPurchaseAnalysesResponse(TypedDict, closed=True):
    analysis_summary_list: NotRequired[
        "aws_sdk_cost_explorer.types.analysis_summary_list.AnalysisSummaryList"
    ]
    """<p>The list of analyses.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommitmentPurchaseAnalysesResponse) -> dict:
    out: dict = {}
    if "analysis_summary_list" in value:
        import aws_sdk_cost_explorer.types.analysis_summary_list

        out["AnalysisSummaryList"] = (
            aws_sdk_cost_explorer.types.analysis_summary_list.serialize_aws_json_1_1(
                value["analysis_summary_list"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommitmentPurchaseAnalysesResponse:
    out: ListCommitmentPurchaseAnalysesResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisSummaryList" in data:
        import aws_sdk_cost_explorer.types.analysis_summary_list

        out["analysis_summary_list"] = (
            aws_sdk_cost_explorer.types.analysis_summary_list.deserialize_aws_json_1_1(
                data["AnalysisSummaryList"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
