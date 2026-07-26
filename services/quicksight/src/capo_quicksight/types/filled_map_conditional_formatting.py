"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapConditionalFormatting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.filled_map_conditional_formatting_option_list


class FilledMapConditionalFormatting(TypedDict, closed=True):
    conditional_formatting_options: "capo_quicksight.types.filled_map_conditional_formatting_option_list.FilledMapConditionalFormattingOptionList"
    """<p>Conditional formatting options of a <code>FilledMapVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapConditionalFormatting) -> dict:
    out: dict = {}
    import capo_quicksight.types.filled_map_conditional_formatting_option_list

    out["ConditionalFormattingOptions"] = (
        capo_quicksight.types.filled_map_conditional_formatting_option_list.serialize_json(
            value["conditional_formatting_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> FilledMapConditionalFormatting:
    out: FilledMapConditionalFormatting = {}  # type: ignore[typeddict-item]
    if "ConditionalFormattingOptions" in data:
        import capo_quicksight.types.filled_map_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            capo_quicksight.types.filled_map_conditional_formatting_option_list.deserialize_json(
                data["ConditionalFormattingOptions"]
            )
        )
    else:
        raise DeserializationError(
            "FilledMapConditionalFormatting.conditional_formatting_options required"
        )
    return out
