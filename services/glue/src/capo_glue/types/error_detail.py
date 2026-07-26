"""Generated from Smithy shape ``com.amazonaws.glue#ErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.name_string


class ErrorDetail(TypedDict, closed=True):
    error_code: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The code associated with this error.</p>"""
    error_message: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A message describing the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
