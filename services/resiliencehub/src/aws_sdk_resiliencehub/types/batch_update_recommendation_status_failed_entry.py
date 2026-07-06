"""Generated from Smithy shape ``com.amazonaws.resiliencehub#BatchUpdateRecommendationStatusFailedEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.error_message
    import aws_sdk_resiliencehub.types.string255


class BatchUpdateRecommendationStatusFailedEntry(TypedDict, closed=True):
    entry_id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>An identifier of an entry in this batch that is used to communicate the result.</p> <note> <p>The <code>entryId</code>s of a batch request need to be unique within a request.</p> </note>"""
    error_message: "aws_sdk_resiliencehub.types.error_message.ErrorMessage"
    """<p>Indicates the error that occurred while excluding an operational recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRecommendationStatusFailedEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateRecommendationStatusFailedEntry:
    out: BatchUpdateRecommendationStatusFailedEntry = {}  # type: ignore[typeddict-item]
    if "entryId" in data:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "BatchUpdateRecommendationStatusFailedEntry.entry_id required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError(
            "BatchUpdateRecommendationStatusFailedEntry.error_message required"
        )
    return out
