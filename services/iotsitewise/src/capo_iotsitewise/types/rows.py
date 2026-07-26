"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Rows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.row

Rows: TypeAlias = list["capo_iotsitewise.types.row.Row"]


# --- restJson1 ser/de ---
def serialize_json(value: Rows) -> list:
    import capo_iotsitewise.types.row

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.row.serialize_json(item))
    return out


def deserialize_json(data: list) -> Rows:
    import capo_iotsitewise.types.row

    out: Rows = []
    for item in data:
        out.append(capo_iotsitewise.types.row.deserialize_json(item))
    return out
