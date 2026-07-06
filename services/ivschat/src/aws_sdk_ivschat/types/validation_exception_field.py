"""Generated from Smithy shape ``com.amazonaws.ivschat#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.error_message
    import aws_sdk_ivschat.types.field_name


class ValidationExceptionField(TypedDict, closed=True):
    name: "aws_sdk_ivschat.types.field_name.FieldName"
    """<p>Name of the field which failed validation.</p>"""
    message: "aws_sdk_ivschat.types.error_message.ErrorMessage"
    """<p>Explanation of the reason for the validation error.</p>"""


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
