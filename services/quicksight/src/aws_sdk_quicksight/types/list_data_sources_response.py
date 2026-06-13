"""Generated from Smithy shape ``com.amazonaws.quicksight#ListDataSourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_source_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListDataSourcesResponse(TypedDict):
    data_sources: NotRequired[
        "aws_sdk_quicksight.types.data_source_list.DataSourceList"
    ]
    """<p>A list of data sources.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourcesResponse) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import aws_sdk_quicksight.types.data_source_list

        out["DataSources"] = aws_sdk_quicksight.types.data_source_list.serialize_json(
            value["data_sources"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListDataSourcesResponse:
    out: ListDataSourcesResponse = {}  # type: ignore[typeddict-item]
    if "DataSources" in data:
        import aws_sdk_quicksight.types.data_source_list

        out["data_sources"] = (
            aws_sdk_quicksight.types.data_source_list.deserialize_json(
                data["DataSources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
