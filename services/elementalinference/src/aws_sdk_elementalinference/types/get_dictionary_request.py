"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetDictionaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_id


class GetDictionaryRequest(TypedDict):
    id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDictionaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDictionaryRequest:
    out: GetDictionaryRequest = {}  # type: ignore[typeddict-item]
    return out
