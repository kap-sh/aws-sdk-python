"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateIngestionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.ingestion_id
    import aws_sdk_quicksight.types.ingestion_type
    import aws_sdk_quicksight.types.string


class CreateIngestionRequest(TypedDict, closed=True):
    data_set_id: "aws_sdk_quicksight.types.string.String"
    """<p>The ID of the dataset used in the ingestion.</p>"""
    ingestion_id: "aws_sdk_quicksight.types.ingestion_id.IngestionId"
    """<p>An ID for the ingestion.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    ingestion_type: NotRequired["aws_sdk_quicksight.types.ingestion_type.IngestionType"]
    """<p>The type of ingestion that you want to create.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIngestionRequest) -> dict:
    out: dict = {}
    if "ingestion_type" in value:
        import aws_sdk_quicksight.types.ingestion_type

        out["IngestionType"] = aws_sdk_quicksight.types.ingestion_type.serialize_json(
            value["ingestion_type"]
        )
    return out


def deserialize_json(data: dict) -> CreateIngestionRequest:
    out: CreateIngestionRequest = {}  # type: ignore[typeddict-item]
    if "IngestionType" in data:
        import aws_sdk_quicksight.types.ingestion_type

        out["ingestion_type"] = (
            aws_sdk_quicksight.types.ingestion_type.deserialize_json(
                data["IngestionType"]
            )
        )
    return out
