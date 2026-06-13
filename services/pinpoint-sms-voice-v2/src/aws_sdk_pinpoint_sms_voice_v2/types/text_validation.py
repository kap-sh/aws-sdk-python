"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#TextValidation``."""

from typing import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError


class TextValidation(TypedDict):
    min_length: "int"
    """<p>The minimum number of characters for the text field.</p>"""
    max_length: "int"
    """<p>The maximum number of characters for the text field.</p>"""
    pattern: "str"
    """<p>The regular expression used to validate the text field.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TextValidation) -> dict:
    out: dict = {}
    out["MinLength"] = value["min_length"]
    out["MaxLength"] = value["max_length"]
    out["Pattern"] = value["pattern"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TextValidation:
    out: TextValidation = {}  # type: ignore[typeddict-item]
    if "MinLength" in data:
        out["min_length"] = data["MinLength"]
    else:
        raise DeserializationError("TextValidation.min_length required")
    if "MaxLength" in data:
        out["max_length"] = data["MaxLength"]
    else:
        raise DeserializationError("TextValidation.max_length required")
    if "Pattern" in data:
        out["pattern"] = data["Pattern"]
    else:
        raise DeserializationError("TextValidation.pattern required")
    return out
