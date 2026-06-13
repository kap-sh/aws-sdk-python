"""Generated from Smithy shape ``com.amazonaws.quicksight#CancelIngestionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.ingestion_id
    import aws_sdk_quicksight.types.string


class CancelIngestionRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_set_id: "aws_sdk_quicksight.types.string.String"
    """<p>The ID of the dataset used in the ingestion.</p>"""
    ingestion_id: "aws_sdk_quicksight.types.ingestion_id.IngestionId"
    """<p>An ID for the ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelIngestionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelIngestionRequest:
    out: CancelIngestionRequest = {}  # type: ignore[typeddict-item]
    return out
