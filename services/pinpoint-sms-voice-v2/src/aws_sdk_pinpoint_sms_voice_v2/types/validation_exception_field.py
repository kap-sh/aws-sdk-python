"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ValidationExceptionField``."""

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The name of the field.</p>"""
    message: "str"
    """<p>The message associated with the validation exception with information to help determine its cause.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
