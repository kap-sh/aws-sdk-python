"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ErrorDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.error_message


class ErrorDetail(TypedDict):
    error_message: NotRequired["aws_sdk_resiliencehub.types.error_message.ErrorMessage"]
    """<p>Provides additional information about the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
