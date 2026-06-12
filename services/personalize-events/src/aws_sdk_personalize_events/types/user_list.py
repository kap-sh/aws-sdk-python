"""Generated from Smithy shape ``com.amazonaws.personalizeevents#UserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.user

UserList: TypeAlias = list["aws_sdk_personalize_events.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: UserList) -> list:
    import aws_sdk_personalize_events.types.user

    out: list = []
    for item in value:
        out.append(aws_sdk_personalize_events.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserList:
    import aws_sdk_personalize_events.types.user

    out: UserList = []
    for item in data:
        out.append(aws_sdk_personalize_events.types.user.deserialize_json(item))
    return out
