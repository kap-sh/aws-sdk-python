"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchDataSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_summary_list
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class SearchDataSetsResponse(TypedDict, closed=True):
    data_set_summaries: NotRequired[
        "capo_quicksight.types.data_set_summary_list.DataSetSummaryList"
    ]
    """<p>A <code>DataSetSummaries</code> object that returns a summary of a dataset.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDataSetsResponse) -> dict:
    out: dict = {}
    if "data_set_summaries" in value:
        import capo_quicksight.types.data_set_summary_list

        out["DataSetSummaries"] = (
            capo_quicksight.types.data_set_summary_list.serialize_json(
                value["data_set_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchDataSetsResponse:
    out: SearchDataSetsResponse = {}  # type: ignore[typeddict-item]
    if "DataSetSummaries" in data:
        import capo_quicksight.types.data_set_summary_list

        out["data_set_summaries"] = (
            capo_quicksight.types.data_set_summary_list.deserialize_json(
                data["DataSetSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
