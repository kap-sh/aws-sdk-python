"""Generated from Smithy shape ``com.amazonaws.securityir#ValidationExceptionField``."""

from typing import TypedDict

from aws_sdk_security_ir.errors import DeserializationError


class ValidationExceptionField(TypedDict):
    name: "str"
    """<p/>"""
    message: "str"
    """<p/>"""


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
