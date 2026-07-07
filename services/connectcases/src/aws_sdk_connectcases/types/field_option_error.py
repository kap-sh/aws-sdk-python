"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldOptionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_option_value


class FieldOptionError(TypedDict, closed=True):
    message: "str"
    """<p>Error message from creating or updating field option.</p>"""
    error_code: "str"
    """<p>Error code from creating or updating field option.</p>"""
    value: "aws_sdk_connectcases.types.field_option_value.FieldOptionValue"
    """<p>The field option value that caused the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldOptionError) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["errorCode"] = value["error_code"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> FieldOptionError:
    out: FieldOptionError = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("FieldOptionError.message required")
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("FieldOptionError.error_code required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("FieldOptionError.value required")
    return out
