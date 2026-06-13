"""Generated from Smithy shape ``com.amazonaws.quicksight#TableConditionalFormatting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_conditional_formatting_option_list


class TableConditionalFormatting(TypedDict):
    conditional_formatting_options: NotRequired[
        "aws_sdk_quicksight.types.table_conditional_formatting_option_list.TableConditionalFormattingOptionList"
    ]
    """<p>Conditional formatting options for a <code>PivotTableVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableConditionalFormatting) -> dict:
    out: dict = {}
    if "conditional_formatting_options" in value:
        import aws_sdk_quicksight.types.table_conditional_formatting_option_list

        out["ConditionalFormattingOptions"] = (
            aws_sdk_quicksight.types.table_conditional_formatting_option_list.serialize_json(
                value["conditional_formatting_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableConditionalFormatting:
    out: TableConditionalFormatting = {}  # type: ignore[typeddict-item]
    if "ConditionalFormattingOptions" in data:
        import aws_sdk_quicksight.types.table_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            aws_sdk_quicksight.types.table_conditional_formatting_option_list.deserialize_json(
                data["ConditionalFormattingOptions"]
            )
        )
    return out
