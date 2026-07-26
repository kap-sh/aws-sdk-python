"""Generated from Smithy shape ``com.amazonaws.iot#ErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.code
    import capo_iot.types.ota_update_error_message


class ErrorInfo(TypedDict, closed=True):
    code: NotRequired["capo_iot.types.code.Code"]
    """<p>The error code.</p>"""
    message: NotRequired[
        "capo_iot.types.ota_update_error_message.OTAUpdateErrorMessage"
    ]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorInfo) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
