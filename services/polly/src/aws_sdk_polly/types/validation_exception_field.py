"""Generated from Smithy shape ``com.amazonaws.polly#ValidationExceptionField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_polly.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_polly.types.validation_exception_field_message
    import aws_sdk_polly.types.validation_exception_field_name


class ValidationExceptionField(TypedDict):
    name: "aws_sdk_polly.types.validation_exception_field_name.ValidationExceptionFieldName"
    """<p>The name of the field that failed validation.</p>"""
    message: "aws_sdk_polly.types.validation_exception_field_message.ValidationExceptionFieldMessage"
    """<p>A message describing why the field failed validation.</p>"""


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
