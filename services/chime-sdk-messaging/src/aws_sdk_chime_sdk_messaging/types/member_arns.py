"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MemberArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn

MemberArns: TypeAlias = list["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]


# --- restJson1 ser/de ---
def serialize_json(value: MemberArns) -> list:
    return list(value)


def deserialize_json(data: list) -> MemberArns:
    return list(data)
