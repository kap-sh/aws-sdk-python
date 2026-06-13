"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_source
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeDataSourceResponse(TypedDict):
    data_source: NotRequired["aws_sdk_quicksight.types.data_source.DataSource"]
    """<p>The information on the data source.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSourceResponse) -> dict:
    out: dict = {}
    if "data_source" in value:
        import aws_sdk_quicksight.types.data_source

        out["DataSource"] = aws_sdk_quicksight.types.data_source.serialize_json(
            value["data_source"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDataSourceResponse:
    out: DescribeDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import aws_sdk_quicksight.types.data_source

        out["data_source"] = aws_sdk_quicksight.types.data_source.deserialize_json(
            data["DataSource"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
