"""Generated from Smithy shape ``com.amazonaws.elementalinference#ExportDictionaryEntriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_entries_payload


class ExportDictionaryEntriesResponse(TypedDict, closed=True):
    entries: NotRequired[
        "aws_sdk_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
    ]
    """<p>The dictionary entries payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportDictionaryEntriesResponse) -> dict:
    out: dict = {}
    if "entries" in value:
        out["entries"] = value["entries"]
    return out


def deserialize_json(data: dict) -> ExportDictionaryEntriesResponse:
    out: ExportDictionaryEntriesResponse = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        out["entries"] = data["entries"]
    return out
