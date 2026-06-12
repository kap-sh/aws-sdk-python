"""Generated from Smithy shape ``com.amazonaws.glacier#NotificationEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string

NotificationEventList: TypeAlias = list["aws_sdk_glacier.types.string.string"]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationEventList) -> list:
    return list(value)


def deserialize_json(data: list) -> NotificationEventList:
    return list(data)
