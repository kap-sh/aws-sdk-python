"""Generated from Smithy shape ``com.amazonaws.mq#__listOfUser``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.user

__listOfUser: TypeAlias = list["capo_mq.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUser) -> list:
    import capo_mq.types.user

    out: list = []
    for item in value:
        out.append(capo_mq.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUser:
    import capo_mq.types.user

    out: __listOfUser = []
    for item in data:
        out.append(capo_mq.types.user.deserialize_json(item))
    return out
