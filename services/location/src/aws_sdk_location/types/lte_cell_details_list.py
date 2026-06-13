"""Generated from Smithy shape ``com.amazonaws.location#LteCellDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.lte_cell_details

LteCellDetailsList: TypeAlias = list[
    "aws_sdk_location.types.lte_cell_details.LteCellDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: LteCellDetailsList) -> list:
    import aws_sdk_location.types.lte_cell_details

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.lte_cell_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> LteCellDetailsList:
    import aws_sdk_location.types.lte_cell_details

    out: LteCellDetailsList = []
    for item in data:
        out.append(aws_sdk_location.types.lte_cell_details.deserialize_json(item))
    return out
