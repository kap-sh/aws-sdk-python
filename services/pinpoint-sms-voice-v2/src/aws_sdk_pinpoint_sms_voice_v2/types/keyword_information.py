"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#KeywordInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_action
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_message


class KeywordInformation(TypedDict, closed=True):
    keyword: "aws_sdk_pinpoint_sms_voice_v2.types.keyword.Keyword"
    """<p>The keyword as a string.</p>"""
    keyword_message: (
        "aws_sdk_pinpoint_sms_voice_v2.types.keyword_message.KeywordMessage"
    )
    """<p>A custom message that can be used with the keyword.</p>"""
    keyword_action: "aws_sdk_pinpoint_sms_voice_v2.types.keyword_action.KeywordAction"
    """<p>The action to perform for the keyword.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeywordInformation) -> dict:
    out: dict = {}
    out["Keyword"] = value["keyword"]
    out["KeywordMessage"] = value["keyword_message"]
    out["KeywordAction"] = value["keyword_action"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KeywordInformation:
    out: KeywordInformation = {}  # type: ignore[typeddict-item]
    if "Keyword" in data:
        out["keyword"] = data["Keyword"]
    else:
        raise DeserializationError("KeywordInformation.keyword required")
    if "KeywordMessage" in data:
        out["keyword_message"] = data["KeywordMessage"]
    else:
        raise DeserializationError("KeywordInformation.keyword_message required")
    if "KeywordAction" in data:
        out["keyword_action"] = data["KeywordAction"]
    else:
        raise DeserializationError("KeywordInformation.keyword_action required")
    return out
