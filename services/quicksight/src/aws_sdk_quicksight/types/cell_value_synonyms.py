"""Generated from Smithy shape ``com.amazonaws.quicksight#CellValueSynonyms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.cell_value_synonym

CellValueSynonyms: TypeAlias = list[
    "aws_sdk_quicksight.types.cell_value_synonym.CellValueSynonym"
]


# --- restJson1 ser/de ---
def serialize_json(value: CellValueSynonyms) -> list:
    import aws_sdk_quicksight.types.cell_value_synonym

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.cell_value_synonym.serialize_json(item))
    return out


def deserialize_json(data: list) -> CellValueSynonyms:
    import aws_sdk_quicksight.types.cell_value_synonym

    out: CellValueSynonyms = []
    for item in data:
        out.append(aws_sdk_quicksight.types.cell_value_synonym.deserialize_json(item))
    return out
