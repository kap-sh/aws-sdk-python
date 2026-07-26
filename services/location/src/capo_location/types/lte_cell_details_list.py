"""Generated from Smithy shape ``com.amazonaws.location#LteCellDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.lte_cell_details

LteCellDetailsList: TypeAlias = list[
    "capo_location.types.lte_cell_details.LteCellDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: LteCellDetailsList) -> list:
    import capo_location.types.lte_cell_details

    out: list = []
    for item in value:
        out.append(capo_location.types.lte_cell_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> LteCellDetailsList:
    import capo_location.types.lte_cell_details

    out: LteCellDetailsList = []
    for item in data:
        out.append(capo_location.types.lte_cell_details.deserialize_json(item))
    return out
