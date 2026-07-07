"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ValidationExceptionField``."""

from typing_extensions import TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError


class ValidationExceptionField(TypedDict, closed=True):
    name: "str"
    """<p>The name of the field that failed validation.</p>"""
    code: "str"
    """<p>The validation error code for the field.</p>"""
    message: "str"
    """<p>A descriptive message about the validation error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ValidationExceptionField.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
