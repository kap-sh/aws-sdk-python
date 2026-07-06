"""Generated from Smithy shape ``com.amazonaws.location#ValidationExceptionField``."""

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The field name where the invalid entry was detected.</p>"""
    message: "str"
    """<p>A message with the reason for the validation exception error.</p>"""


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
