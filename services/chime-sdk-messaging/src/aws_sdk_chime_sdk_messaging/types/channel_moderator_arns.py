"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelModeratorArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn

ChannelModeratorArns: TypeAlias = list[
    "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelModeratorArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ChannelModeratorArns:
    return list(data)
