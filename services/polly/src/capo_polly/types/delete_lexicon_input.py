"""Generated from Smithy shape ``com.amazonaws.polly#DeleteLexiconInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_polly.types.lexicon_name


class DeleteLexiconInput(TypedDict, closed=True):
    name: "capo_polly.types.lexicon_name.LexiconName"
    """<p>The name of the lexicon to delete. Must be an existing lexicon in the region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLexiconInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLexiconInput:
    out: DeleteLexiconInput = {}  # type: ignore[typeddict-item]
    return out
