"""Generated from Smithy shape ``com.amazonaws.greengrass#ErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class ErrorDetail(TypedDict, closed=True):
    detailed_error_code: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A detailed error code."""
    detailed_error_message: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A detailed error message."""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    if "detailed_error_code" in value:
        out["DetailedErrorCode"] = value["detailed_error_code"]
    if "detailed_error_message" in value:
        out["DetailedErrorMessage"] = value["detailed_error_message"]
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "DetailedErrorCode" in data:
        out["detailed_error_code"] = data["DetailedErrorCode"]
    if "DetailedErrorMessage" in data:
        out["detailed_error_message"] = data["DetailedErrorMessage"]
    return out
