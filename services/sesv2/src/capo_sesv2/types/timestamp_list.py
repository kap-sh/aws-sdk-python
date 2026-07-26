"""Generated from Smithy shape ``com.amazonaws.sesv2#TimestampList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.timestamp

TimestampList: TypeAlias = list["capo_sesv2.types.timestamp.Timestamp"]


# --- restJson1 ser/de ---
def serialize_json(value: TimestampList) -> list:
    import capo_sesv2.types.timestamp

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.timestamp.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimestampList:
    import capo_sesv2.types.timestamp

    out: TimestampList = []
    for item in data:
        out.append(capo_sesv2.types.timestamp.deserialize_json(item))
    return out
