"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomInstruction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.inline_custom_instruction


class CustomInstruction(TypedDict):
    inline_custom_instruction: NotRequired[
        "aws_sdk_quicksight.types.inline_custom_instruction.InlineCustomInstruction"
    ]
    """<p>An inline custom instruction containing text and optional uploaded document metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomInstruction) -> dict:
    out: dict = {}
    if "inline_custom_instruction" in value:
        import aws_sdk_quicksight.types.inline_custom_instruction

        out["InlineCustomInstruction"] = (
            aws_sdk_quicksight.types.inline_custom_instruction.serialize_json(
                value["inline_custom_instruction"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomInstruction:
    out: CustomInstruction = {}  # type: ignore[typeddict-item]
    if "InlineCustomInstruction" in data:
        import aws_sdk_quicksight.types.inline_custom_instruction

        out["inline_custom_instruction"] = (
            aws_sdk_quicksight.types.inline_custom_instruction.deserialize_json(
                data["InlineCustomInstruction"]
            )
        )
    return out
