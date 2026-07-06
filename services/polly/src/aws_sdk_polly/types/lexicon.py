"""Generated from Smithy shape ``com.amazonaws.polly#Lexicon``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.lexicon_content
    import aws_sdk_polly.types.lexicon_name


class Lexicon(TypedDict, closed=True):
    content: NotRequired["aws_sdk_polly.types.lexicon_content.LexiconContent"]
    """<p>Lexicon content in string format. The content of a lexicon must be in PLS format.</p>"""
    name: NotRequired["aws_sdk_polly.types.lexicon_name.LexiconName"]
    """<p>Name of the lexicon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Lexicon) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Lexicon:
    out: Lexicon = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
