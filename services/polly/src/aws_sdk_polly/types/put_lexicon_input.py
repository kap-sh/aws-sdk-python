"""Generated from Smithy shape ``com.amazonaws.polly#PutLexiconInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_polly.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_polly.types.lexicon_content
    import aws_sdk_polly.types.lexicon_name


class PutLexiconInput(TypedDict):
    name: "aws_sdk_polly.types.lexicon_name.LexiconName"
    """<p>Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. </p>"""
    content: "aws_sdk_polly.types.lexicon_content.LexiconContent"
    """<p>Content of the PLS lexicon as string data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutLexiconInput) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    return out


def deserialize_json(data: dict) -> PutLexiconInput:
    out: PutLexiconInput = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("PutLexiconInput.content required")
    return out
