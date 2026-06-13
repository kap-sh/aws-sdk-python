"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapConditionalFormatting``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filled_map_conditional_formatting_option_list


class FilledMapConditionalFormatting(TypedDict):
    conditional_formatting_options: "aws_sdk_quicksight.types.filled_map_conditional_formatting_option_list.FilledMapConditionalFormattingOptionList"
    """<p>Conditional formatting options of a <code>FilledMapVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapConditionalFormatting) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.filled_map_conditional_formatting_option_list

    out["ConditionalFormattingOptions"] = (
        aws_sdk_quicksight.types.filled_map_conditional_formatting_option_list.serialize_json(
            value["conditional_formatting_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> FilledMapConditionalFormatting:
    out: FilledMapConditionalFormatting = {}  # type: ignore[typeddict-item]
    if "ConditionalFormattingOptions" in data:
        import aws_sdk_quicksight.types.filled_map_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            aws_sdk_quicksight.types.filled_map_conditional_formatting_option_list.deserialize_json(
                data["ConditionalFormattingOptions"]
            )
        )
    else:
        raise DeserializationError(
            "FilledMapConditionalFormatting.conditional_formatting_options required"
        )
    return out
