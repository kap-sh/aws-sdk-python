"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDataSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateDataSetResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    data_set_id: NotRequired["aws_sdk_quicksight.types.resource_id.ResourceId"]
    """<p>The ID for the dataset that you want to update. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    ingestion_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.</p>"""
    ingestion_id: NotRequired["aws_sdk_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSetResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "ingestion_arn" in value:
        out["IngestionArn"] = value["ingestion_arn"]
    if "ingestion_id" in value:
        out["IngestionId"] = value["ingestion_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateDataSetResponse:
    out: UpdateDataSetResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    if "IngestionArn" in data:
        out["ingestion_arn"] = data["IngestionArn"]
    if "IngestionId" in data:
        out["ingestion_id"] = data["IngestionId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
