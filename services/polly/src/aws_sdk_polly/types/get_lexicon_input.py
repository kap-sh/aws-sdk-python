"""Generated from Smithy shape ``com.amazonaws.polly#GetLexiconInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.lexicon_name


class GetLexiconInput(TypedDict):
    name: "aws_sdk_polly.types.lexicon_name.LexiconName"
    """<p>Name of the lexicon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLexiconInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLexiconInput:
    out: GetLexiconInput = {}  # type: ignore[typeddict-item]
    return out
