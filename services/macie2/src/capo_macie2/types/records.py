"""Generated from Smithy shape ``com.amazonaws.macie2#Records``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.record

Records: TypeAlias = list["capo_macie2.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: Records) -> list:
    import capo_macie2.types.record

    out: list = []
    for item in value:
        out.append(capo_macie2.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> Records:
    import capo_macie2.types.record

    out: Records = []
    for item in data:
        out.append(capo_macie2.types.record.deserialize_json(item))
    return out
