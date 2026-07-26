"""Generated from Smithy shape ``com.amazonaws.datazone#CellOrder``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.cell_information

CellOrder: TypeAlias = list["capo_datazone.types.cell_information.CellInformation"]


# --- restJson1 ser/de ---
def serialize_json(value: CellOrder) -> list:
    import capo_datazone.types.cell_information

    out: list = []
    for item in value:
        out.append(capo_datazone.types.cell_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> CellOrder:
    import capo_datazone.types.cell_information

    out: CellOrder = []
    for item in data:
        out.append(capo_datazone.types.cell_information.deserialize_json(item))
    return out
