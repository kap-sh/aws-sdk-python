"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id


class FieldError(TypedDict):
    id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>The field identifier that caused the error.</p>"""
    error_code: "str"
    """<p>The error code from getting a field.</p>"""
    message: NotRequired["str"]
    """<p>The error message from getting a field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldError) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FieldError:
    out: FieldError = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FieldError.id required")
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("FieldError.error_code required")
    if "message" in data:
        out["message"] = data["message"]
    return out
