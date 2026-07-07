"""Generated from Smithy shape ``com.amazonaws.appsync#ErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.error_message


class ErrorDetail(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appsync.types.error_message.ErrorMessage"]
    """<p>The error payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
