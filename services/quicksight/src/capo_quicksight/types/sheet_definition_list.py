"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_definition

SheetDefinitionList: TypeAlias = list[
    "capo_quicksight.types.sheet_definition.SheetDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetDefinitionList) -> list:
    import capo_quicksight.types.sheet_definition

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.sheet_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> SheetDefinitionList:
    import capo_quicksight.types.sheet_definition

    out: SheetDefinitionList = []
    for item in data:
        out.append(capo_quicksight.types.sheet_definition.deserialize_json(item))
    return out
