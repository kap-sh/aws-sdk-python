"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ValidationExceptionField``."""

from typing import TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError


class ValidationExceptionField(TypedDict):
    name: "str"
    """<p>Name of the field that failed validation.</p>"""
    reason: "str"
    """<p>Reason for the validation failure.</p>"""
    message: "str"
    """<p>Detailed error message describing the validation issue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Reason"] = value["reason"]
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "Reason" in data:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("ValidationExceptionField.reason required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
