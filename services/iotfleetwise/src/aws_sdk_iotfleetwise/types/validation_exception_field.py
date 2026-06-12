"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ValidationExceptionField``."""

from typing import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError


class ValidationExceptionField(TypedDict):
    name: "str"
    """<p>The name of the parameter field with the validation error.</p>"""
    message: "str"
    """<p>A message about the validation error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
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
