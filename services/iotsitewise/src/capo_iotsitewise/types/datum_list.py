"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatumList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.datum

DatumList: TypeAlias = list["capo_iotsitewise.types.datum.Datum"]


# --- restJson1 ser/de ---
def serialize_json(value: DatumList) -> list:
    import capo_iotsitewise.types.datum

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.datum.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatumList:
    import capo_iotsitewise.types.datum

    out: DatumList = []
    for item in data:
        out.append(capo_iotsitewise.types.datum.deserialize_json(item))
    return out
