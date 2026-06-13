"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DeleteDataSourceResponse(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the data source that you deleted.</p>"""
    data_source_id: NotRequired["aws_sdk_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteDataSourceResponse:
    out: DeleteDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
