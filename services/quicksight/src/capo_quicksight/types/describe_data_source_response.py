"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_source
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeDataSourceResponse(TypedDict, closed=True):
    data_source: NotRequired["capo_quicksight.types.data_source.DataSource"]
    """<p>The information on the data source.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_quicksight.types.data_source

        out["DataSource"] = capo_quicksight.types.data_source.serialize_json(
            value["data_source"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDataSourceResponse:
    out: DescribeDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import capo_quicksight.types.data_source

        out["data_source"] = capo_quicksight.types.data_source.deserialize_json(
            data["DataSource"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
