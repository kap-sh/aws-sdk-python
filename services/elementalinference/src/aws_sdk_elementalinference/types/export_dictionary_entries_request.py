"""Generated from Smithy shape ``com.amazonaws.elementalinference#ExportDictionaryEntriesRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_id


class ExportDictionaryEntriesRequest(TypedDict):
    id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary whose entries you want to export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportDictionaryEntriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportDictionaryEntriesRequest:
    out: ExportDictionaryEntriesRequest = {}  # type: ignore[typeddict-item]
    return out
