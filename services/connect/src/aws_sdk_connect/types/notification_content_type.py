"""Generated from Smithy shape ``com.amazonaws.connect#NotificationContentType``."""

from typing import Literal, TypeAlias, cast

NotificationContentType: TypeAlias = Literal["PLAIN_TEXT",]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationContentType) -> str:
    return value


def deserialize_json(data: str) -> NotificationContentType:
    return cast(NotificationContentType, data)
