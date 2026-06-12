"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchItemError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.string


class BatchItemError(TypedDict):
    index: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    error_code: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>The numeric error code of the error.</p>"""
    error_message: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>A text description of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchItemError) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchItemError:
    out: BatchItemError = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
