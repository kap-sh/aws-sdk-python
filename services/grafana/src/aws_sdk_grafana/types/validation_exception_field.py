"""Generated from Smithy shape ``com.amazonaws.grafana#ValidationExceptionField``."""

from typing import TypedDict

from aws_sdk_grafana.errors import DeserializationError


class ValidationExceptionField(TypedDict):
    name: "str"
    """<p>The name of the field that caused the validation error.</p>"""
    message: "str"
    """<p>A message describing why this field couldn't be validated.</p>"""


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
