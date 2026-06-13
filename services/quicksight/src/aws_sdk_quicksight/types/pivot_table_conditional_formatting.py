"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormatting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_option_list


class PivotTableConditionalFormatting(TypedDict):
    conditional_formatting_options: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_conditional_formatting_option_list.PivotTableConditionalFormattingOptionList"
    ]
    """<p>Conditional formatting options for a <code>PivotTableVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormatting) -> dict:
    out: dict = {}
    if "conditional_formatting_options" in value:
        import aws_sdk_quicksight.types.pivot_table_conditional_formatting_option_list

        out["ConditionalFormattingOptions"] = (
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_option_list.serialize_json(
                value["conditional_formatting_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableConditionalFormatting:
    out: PivotTableConditionalFormatting = {}  # type: ignore[typeddict-item]
    if "ConditionalFormattingOptions" in data:
        import aws_sdk_quicksight.types.pivot_table_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_option_list.deserialize_json(
                data["ConditionalFormattingOptions"]
            )
        )
    return out
