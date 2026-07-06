"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.tool_example_list


class ToolInstruction(TypedDict, closed=True):
    instruction: NotRequired["str"]
    """<p>The instruction text for the tool.</p>"""
    examples: NotRequired["aws_sdk_qconnect.types.tool_example_list.ToolExampleList"]
    """<p>Examples for using the tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolInstruction) -> dict:
    out: dict = {}
    if "instruction" in value:
        out["instruction"] = value["instruction"]
    if "examples" in value:
        import aws_sdk_qconnect.types.tool_example_list

        out["examples"] = aws_sdk_qconnect.types.tool_example_list.serialize_json(
            value["examples"]
        )
    return out


def deserialize_json(data: dict) -> ToolInstruction:
    out: ToolInstruction = {}  # type: ignore[typeddict-item]
    if "instruction" in data:
        out["instruction"] = data["instruction"]
    if "examples" in data:
        import aws_sdk_qconnect.types.tool_example_list

        out["examples"] = aws_sdk_qconnect.types.tool_example_list.deserialize_json(
            data["examples"]
        )
    return out
