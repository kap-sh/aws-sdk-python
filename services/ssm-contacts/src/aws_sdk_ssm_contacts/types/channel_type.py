"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ChannelType``."""

from typing import Literal, TypeAlias, cast

ChannelType: TypeAlias = Literal[
    "SMS",
    "VOICE",
    "EMAIL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChannelType:
    return cast(ChannelType, data)
