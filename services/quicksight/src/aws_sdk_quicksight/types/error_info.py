"""Generated from Smithy shape ``com.amazonaws.quicksight#ErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.ingestion_error_type
    import aws_sdk_quicksight.types.string


class ErrorInfo(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_quicksight.types.ingestion_error_type.IngestionErrorType"
    ]
    """<p>Error type.</p>"""
    message: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>Error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorInfo) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_quicksight.types.ingestion_error_type

        out["Type"] = aws_sdk_quicksight.types.ingestion_error_type.serialize_json(
            value["type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_quicksight.types.ingestion_error_type

        out["type"] = aws_sdk_quicksight.types.ingestion_error_type.deserialize_json(
            data["Type"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
