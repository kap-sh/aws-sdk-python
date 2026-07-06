"""Generated from Smithy shape ``com.amazonaws.networkmanager#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.server_side_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    """<p>The name of the field.</p>"""
    message: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    """<p>The message for the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
