"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPromptInputParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.style_description


class CustomPromptInputParameters(TypedDict):
    response_length: NotRequired[
        "aws_sdk_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Instructions for the desired response length.</p>"""
    output_style: NotRequired[
        "aws_sdk_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Instructions for the desired output style.</p>"""
    identity: NotRequired["aws_sdk_quicksight.types.style_description.StyleDescription"]
    """<p>Instructions that define the agent's identity and persona.</p>"""
    tone: NotRequired["aws_sdk_quicksight.types.style_description.StyleDescription"]
    """<p>Instructions for the desired tone of responses.</p>"""
    custom_instructions: NotRequired[
        "aws_sdk_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Custom instructions for the agent's behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPromptInputParameters) -> dict:
    out: dict = {}
    if "response_length" in value:
        out["ResponseLength"] = value["response_length"]
    if "output_style" in value:
        out["OutputStyle"] = value["output_style"]
    if "identity" in value:
        out["Identity"] = value["identity"]
    if "tone" in value:
        out["Tone"] = value["tone"]
    if "custom_instructions" in value:
        out["CustomInstructions"] = value["custom_instructions"]
    return out


def deserialize_json(data: dict) -> CustomPromptInputParameters:
    out: CustomPromptInputParameters = {}  # type: ignore[typeddict-item]
    if "ResponseLength" in data:
        out["response_length"] = data["ResponseLength"]
    if "OutputStyle" in data:
        out["output_style"] = data["OutputStyle"]
    if "Identity" in data:
        out["identity"] = data["Identity"]
    if "Tone" in data:
        out["tone"] = data["Tone"]
    if "CustomInstructions" in data:
        out["custom_instructions"] = data["CustomInstructions"]
    return out
