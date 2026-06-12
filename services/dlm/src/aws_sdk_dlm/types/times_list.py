"""Generated from Smithy shape ``com.amazonaws.dlm#TimesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.time

TimesList: TypeAlias = list["aws_sdk_dlm.types.time.Time"]


# --- restJson1 ser/de ---
def serialize_json(value: TimesList) -> list:
    return list(value)


def deserialize_json(data: list) -> TimesList:
    return list(data)
