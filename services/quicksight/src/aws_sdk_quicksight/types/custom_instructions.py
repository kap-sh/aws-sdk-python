"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomInstructions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_instructions_string


class CustomInstructions(TypedDict, closed=True):
    custom_instructions_string: (
        "aws_sdk_quicksight.types.custom_instructions_string.CustomInstructionsString"
    )
    """<p>A text field for providing additional guidance or context for response generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomInstructions) -> dict:
    out: dict = {}
    out["CustomInstructionsString"] = value["custom_instructions_string"]
    return out


def deserialize_json(data: dict) -> CustomInstructions:
    out: CustomInstructions = {}  # type: ignore[typeddict-item]
    if "CustomInstructionsString" in data:
        out["custom_instructions_string"] = data["CustomInstructionsString"]
    else:
        raise DeserializationError(
            "CustomInstructions.custom_instructions_string required"
        )
    return out
