"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.string

StringList: TypeAlias = list["aws_sdk_chime_sdk_voice.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)
