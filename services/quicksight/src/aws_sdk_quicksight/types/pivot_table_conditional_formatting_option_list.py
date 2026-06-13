"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_option

PivotTableConditionalFormattingOptionList: TypeAlias = list[
    "aws_sdk_quicksight.types.pivot_table_conditional_formatting_option.PivotTableConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormattingOptionList) -> list:
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PivotTableConditionalFormattingOptionList:
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_option

    out: PivotTableConditionalFormattingOptionList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out
