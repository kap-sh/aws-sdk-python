"""Generated from Smithy shape ``com.amazonaws.m2#ValidationExceptionField``."""

from typing import TypedDict

from aws_sdk_m2.errors import DeserializationError


class ValidationExceptionField(TypedDict):
    name: "str"
    """<p>The name of the exception field.</p>"""
    message: "str"
    """<p>The message of the exception field.</p>"""


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
