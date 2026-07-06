"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDataSetPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateDataSetPermissionsResponse(TypedDict, closed=True):
    data_set_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    data_set_id: NotRequired["aws_sdk_quicksight.types.resource_id.ResourceId"]
    """<p>The ID for the dataset whose permissions you want to update. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSetPermissionsResponse) -> dict:
    out: dict = {}
    if "data_set_arn" in value:
        out["DataSetArn"] = value["data_set_arn"]
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateDataSetPermissionsResponse:
    out: UpdateDataSetPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "DataSetArn" in data:
        out["data_set_arn"] = data["DataSetArn"]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
