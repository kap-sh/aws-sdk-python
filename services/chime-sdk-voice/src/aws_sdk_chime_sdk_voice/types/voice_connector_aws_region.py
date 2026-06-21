"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorAwsRegion``."""

from typing import Literal, TypeAlias, cast

VoiceConnectorAwsRegion: TypeAlias = Literal[
    "us-east-1",
    "us-west-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "ap-northeast-2",
    "ap-northeast-1",
    "ap-southeast-1",
    "ap-southeast-2",
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorAwsRegion) -> str:
    return value


def deserialize_json(data: str) -> VoiceConnectorAwsRegion:
    return cast(VoiceConnectorAwsRegion, data)
