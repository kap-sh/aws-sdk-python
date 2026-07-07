"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteDictionaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_id


class DeleteDictionaryRequest(TypedDict, closed=True):
    id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDictionaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDictionaryRequest:
    out: DeleteDictionaryRequest = {}  # type: ignore[typeddict-item]
    return out
