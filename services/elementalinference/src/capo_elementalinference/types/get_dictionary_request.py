"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetDictionaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.dictionary_id


class GetDictionaryRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDictionaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDictionaryRequest:
    out: GetDictionaryRequest = {}  # type: ignore[typeddict-item]
    return out
