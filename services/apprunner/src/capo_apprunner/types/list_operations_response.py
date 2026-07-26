"""Generated from Smithy shape ``com.amazonaws.apprunner#ListOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.operation_summary_list
    import capo_apprunner.types.string


class ListOperationsResponse(TypedDict, closed=True):
    operation_summary_list: NotRequired[
        "capo_apprunner.types.operation_summary_list.OperationSummaryList"
    ]
    """<p>A list of operation summary information records. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["capo_apprunner.types.string.String"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOperationsResponse) -> dict:
    out: dict = {}
    if "operation_summary_list" in value:
        import capo_apprunner.types.operation_summary_list

        out["OperationSummaryList"] = (
            capo_apprunner.types.operation_summary_list.serialize_aws_json_1_0(
                value["operation_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOperationsResponse:
    out: ListOperationsResponse = {}  # type: ignore[typeddict-item]
    if "OperationSummaryList" in data:
        import capo_apprunner.types.operation_summary_list

        out["operation_summary_list"] = (
            capo_apprunner.types.operation_summary_list.deserialize_aws_json_1_0(
                data["OperationSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
