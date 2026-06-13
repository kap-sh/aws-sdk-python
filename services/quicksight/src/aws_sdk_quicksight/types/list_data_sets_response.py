"""Generated from Smithy shape ``com.amazonaws.quicksight#ListDataSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_summary_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListDataSetsResponse(TypedDict):
    data_set_summaries: NotRequired[
        "aws_sdk_quicksight.types.data_set_summary_list.DataSetSummaryList"
    ]
    """<p>The list of dataset summaries.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetsResponse) -> dict:
    out: dict = {}
    if "data_set_summaries" in value:
        import aws_sdk_quicksight.types.data_set_summary_list

        out["DataSetSummaries"] = (
            aws_sdk_quicksight.types.data_set_summary_list.serialize_json(
                value["data_set_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListDataSetsResponse:
    out: ListDataSetsResponse = {}  # type: ignore[typeddict-item]
    if "DataSetSummaries" in data:
        import aws_sdk_quicksight.types.data_set_summary_list

        out["data_set_summaries"] = (
            aws_sdk_quicksight.types.data_set_summary_list.deserialize_json(
                data["DataSetSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
