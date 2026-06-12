"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedLine``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_line_text


class AutomatedReasoningPolicyAnnotatedLine(TypedDict):
    line_number: NotRequired["int"]
    """<p>The line number of this text within the source document.</p>"""
    line_text: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_line_text.AutomatedReasoningPolicyLineText"
    ]
    """<p>The actual text content of this line from the source document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedLine) -> dict:
    out: dict = {}
    if "line_number" in value:
        out["lineNumber"] = value["line_number"]
    if "line_text" in value:
        out["lineText"] = value["line_text"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAnnotatedLine:
    out: AutomatedReasoningPolicyAnnotatedLine = {}  # type: ignore[typeddict-item]
    if "lineNumber" in data:
        out["line_number"] = data["lineNumber"]
    if "lineText" in data:
        out["line_text"] = data["lineText"]
    return out
