"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateDictionaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.dictionary_entries_payload
    import capo_elementalinference.types.dictionary_id
    import capo_elementalinference.types.dictionary_language
    import capo_elementalinference.types.resource_name


class UpdateDictionaryRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary to update.</p>"""
    name: NotRequired["capo_elementalinference.types.resource_name.ResourceName"]
    """<p>A new name for the dictionary. If not specified, the name is not changed.</p>"""
    language: NotRequired[
        "capo_elementalinference.types.dictionary_language.DictionaryLanguage"
    ]
    """<p>A new language for the dictionary. If not specified, the language is not changed.</p>"""
    entries: NotRequired[
        "capo_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
    ]
    """<p>New dictionary entries. If not specified, the entries are not changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDictionaryRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "language" in value:
        import capo_elementalinference.types.dictionary_language

        out["language"] = (
            capo_elementalinference.types.dictionary_language.serialize_json(
                value["language"]
            )
        )
    if "entries" in value:
        out["entries"] = value["entries"]
    return out


def deserialize_json(data: dict) -> UpdateDictionaryRequest:
    out: UpdateDictionaryRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "language" in data:
        import capo_elementalinference.types.dictionary_language

        out["language"] = (
            capo_elementalinference.types.dictionary_language.deserialize_json(
                data["language"]
            )
        )
    if "entries" in data:
        out["entries"] = data["entries"]
    return out
