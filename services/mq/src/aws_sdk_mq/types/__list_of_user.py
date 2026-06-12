"""Generated from Smithy shape ``com.amazonaws.mq#__listOfUser``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.user

__listOfUser: TypeAlias = list["aws_sdk_mq.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUser) -> list:
    import aws_sdk_mq.types.user

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUser:
    import aws_sdk_mq.types.user

    out: __listOfUser = []
    for item in data:
        out.append(aws_sdk_mq.types.user.deserialize_json(item))
    return out
