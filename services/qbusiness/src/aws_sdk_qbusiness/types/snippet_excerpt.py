"""Generated from Smithy shape ``com.amazonaws.qbusiness#SnippetExcerpt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.snippet_excerpt_text


class SnippetExcerpt(TypedDict, closed=True):
    text: NotRequired["aws_sdk_qbusiness.types.snippet_excerpt_text.SnippetExcerptText"]
    """<p>The relevant text excerpt from a source that was used to generate a citation text segment in an Amazon Q chat response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnippetExcerpt) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> SnippetExcerpt:
    out: SnippetExcerpt = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    return out
