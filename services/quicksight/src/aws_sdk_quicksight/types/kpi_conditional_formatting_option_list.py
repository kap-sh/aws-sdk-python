"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.kpi_conditional_formatting_option

KPIConditionalFormattingOptionList: TypeAlias = list[
    "aws_sdk_quicksight.types.kpi_conditional_formatting_option.KPIConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: KPIConditionalFormattingOptionList) -> list:
    import aws_sdk_quicksight.types.kpi_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.kpi_conditional_formatting_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> KPIConditionalFormattingOptionList:
    import aws_sdk_quicksight.types.kpi_conditional_formatting_option

    out: KPIConditionalFormattingOptionList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.kpi_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out
