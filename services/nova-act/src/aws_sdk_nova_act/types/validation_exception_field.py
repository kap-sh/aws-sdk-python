"""Generated from Smithy shape ``com.amazonaws.novaact#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.non_blank_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The name of the field that failed validation.</p>"""
    message: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>A description of the validation error for this field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
