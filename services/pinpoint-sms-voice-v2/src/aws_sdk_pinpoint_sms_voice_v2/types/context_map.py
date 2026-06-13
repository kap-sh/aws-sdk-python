"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.context_key
    import aws_sdk_pinpoint_sms_voice_v2.types.context_value

ContextMap: TypeAlias = dict[
    "aws_sdk_pinpoint_sms_voice_v2.types.context_key.ContextKey",
    "aws_sdk_pinpoint_sms_voice_v2.types.context_value.ContextValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> ContextMap:
    out: ContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
