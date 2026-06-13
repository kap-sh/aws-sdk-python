"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchDataSourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_source_summary_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class SearchDataSourcesResponse(TypedDict):
    data_source_summaries: NotRequired[
        "aws_sdk_quicksight.types.data_source_summary_list.DataSourceSummaryList"
    ]
    """<p>A <code>DataSourceSummaries</code> object that returns a summary of a data source.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDataSourcesResponse) -> dict:
    out: dict = {}
    if "data_source_summaries" in value:
        import aws_sdk_quicksight.types.data_source_summary_list

        out["DataSourceSummaries"] = (
            aws_sdk_quicksight.types.data_source_summary_list.serialize_json(
                value["data_source_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchDataSourcesResponse:
    out: SearchDataSourcesResponse = {}  # type: ignore[typeddict-item]
    if "DataSourceSummaries" in data:
        import aws_sdk_quicksight.types.data_source_summary_list

        out["data_source_summaries"] = (
            aws_sdk_quicksight.types.data_source_summary_list.deserialize_json(
                data["DataSourceSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
