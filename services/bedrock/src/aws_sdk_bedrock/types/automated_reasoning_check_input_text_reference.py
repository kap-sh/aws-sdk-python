"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckInputTextReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_natural_language_statement_content


class AutomatedReasoningCheckInputTextReference(TypedDict, closed=True):
    text: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_natural_language_statement_content.AutomatedReasoningNaturalLanguageStatementContent"
    ]
    """<p>The specific text from the original input that this reference points to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckInputTextReference) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckInputTextReference:
    out: AutomatedReasoningCheckInputTextReference = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    return out
