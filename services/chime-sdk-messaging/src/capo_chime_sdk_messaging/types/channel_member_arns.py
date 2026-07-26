"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMemberArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn

ChannelMemberArns: TypeAlias = list["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMemberArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ChannelMemberArns:
    return list(data)
