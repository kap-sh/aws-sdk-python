"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class CreateDataSourceResponse(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the data source.</p>"""
    data_source_id: NotRequired["aws_sdk_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    creation_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>The status of creating the data source.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "creation_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["CreationStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["creation_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateDataSourceResponse:
    out: CreateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "CreationStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["creation_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["CreationStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
