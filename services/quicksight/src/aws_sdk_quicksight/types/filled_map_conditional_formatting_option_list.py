"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filled_map_conditional_formatting_option

FilledMapConditionalFormattingOptionList: TypeAlias = list[
    "aws_sdk_quicksight.types.filled_map_conditional_formatting_option.FilledMapConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapConditionalFormattingOptionList) -> list:
    import aws_sdk_quicksight.types.filled_map_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.filled_map_conditional_formatting_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FilledMapConditionalFormattingOptionList:
    import aws_sdk_quicksight.types.filled_map_conditional_formatting_option

    out: FilledMapConditionalFormattingOptionList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.filled_map_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out
