"""Generated from Smithy shape ``com.amazonaws.uxc#ValidationExceptionField``."""

from typing_extensions import TypedDict

from aws_sdk_uxc.errors import DeserializationError


class ValidationExceptionField(TypedDict, closed=True):
    path: "str"
    """<p>The field name with the validation exception.</p>"""
    message: "str"
    """<p>A message describing the validation exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("ValidationExceptionField.path required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
