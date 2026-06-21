"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationResourceType``."""

from typing import Literal, TypeAlias, cast

NotificationResourceType: TypeAlias = Literal["PROJECT",]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationResourceType) -> str:
    return value


def deserialize_json(data: str) -> NotificationResourceType:
    return cast(NotificationResourceType, data)
