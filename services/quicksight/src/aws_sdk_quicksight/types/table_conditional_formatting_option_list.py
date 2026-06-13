"""Generated from Smithy shape ``com.amazonaws.quicksight#TableConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_conditional_formatting_option

TableConditionalFormattingOptionList: TypeAlias = list[
    "aws_sdk_quicksight.types.table_conditional_formatting_option.TableConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableConditionalFormattingOptionList) -> list:
    import aws_sdk_quicksight.types.table_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.table_conditional_formatting_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TableConditionalFormattingOptionList:
    import aws_sdk_quicksight.types.table_conditional_formatting_option

    out: TableConditionalFormattingOptionList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.table_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out
