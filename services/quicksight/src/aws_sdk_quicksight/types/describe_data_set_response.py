"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeDataSetResponse(TypedDict):
    data_set: NotRequired["aws_sdk_quicksight.types.data_set.DataSet"]
    """<p>Information on the dataset.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSetResponse) -> dict:
    out: dict = {}
    if "data_set" in value:
        import aws_sdk_quicksight.types.data_set

        out["DataSet"] = aws_sdk_quicksight.types.data_set.serialize_json(
            value["data_set"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDataSetResponse:
    out: DescribeDataSetResponse = {}  # type: ignore[typeddict-item]
    if "DataSet" in data:
        import aws_sdk_quicksight.types.data_set

        out["data_set"] = aws_sdk_quicksight.types.data_set.deserialize_json(
            data["DataSet"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
