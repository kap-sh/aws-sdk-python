"""Generated from Smithy shape ``com.amazonaws.quicksight#CancelIngestionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.ingestion_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class CancelIngestionResponse(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the data ingestion.</p>"""
    ingestion_id: NotRequired["aws_sdk_quicksight.types.ingestion_id.IngestionId"]
    """<p>An ID for the ingestion.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelIngestionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "ingestion_id" in value:
        out["IngestionId"] = value["ingestion_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CancelIngestionResponse:
    out: CancelIngestionResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "IngestionId" in data:
        out["ingestion_id"] = data["IngestionId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
