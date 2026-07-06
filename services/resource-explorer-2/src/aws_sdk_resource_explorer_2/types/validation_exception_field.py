"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ValidationExceptionField``."""

from typing_extensions import TypedDict

from aws_sdk_resource_explorer_2.errors import DeserializationError


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The name of the request field that had a validation error.</p>"""
    validation_issue: "str"
    """<p>The validation error caused by the request field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ValidationIssue"] = value["validation_issue"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "ValidationIssue" in data:
        out["validation_issue"] = data["ValidationIssue"]
    else:
        raise DeserializationError("ValidationExceptionField.validation_issue required")
    return out
