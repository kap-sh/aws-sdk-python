"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipSheetDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.tooltip_sheet_definition

TooltipSheetDefinitionList: TypeAlias = list[
    "aws_sdk_quicksight.types.tooltip_sheet_definition.TooltipSheetDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipSheetDefinitionList) -> list:
    import aws_sdk_quicksight.types.tooltip_sheet_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.tooltip_sheet_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TooltipSheetDefinitionList:
    import aws_sdk_quicksight.types.tooltip_sheet_definition

    out: TooltipSheetDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.tooltip_sheet_definition.deserialize_json(item)
        )
    return out
