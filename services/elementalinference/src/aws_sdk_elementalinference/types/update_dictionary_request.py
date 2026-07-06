"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateDictionaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_entries_payload
    import aws_sdk_elementalinference.types.dictionary_id
    import aws_sdk_elementalinference.types.dictionary_language
    import aws_sdk_elementalinference.types.resource_name


class UpdateDictionaryRequest(TypedDict, closed=True):
    id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary to update.</p>"""
    name: NotRequired["aws_sdk_elementalinference.types.resource_name.ResourceName"]
    """<p>A new name for the dictionary. If not specified, the name is not changed.</p>"""
    language: NotRequired[
        "aws_sdk_elementalinference.types.dictionary_language.DictionaryLanguage"
    ]
    """<p>A new language for the dictionary. If not specified, the language is not changed.</p>"""
    entries: NotRequired[
        "aws_sdk_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
    ]
    """<p>New dictionary entries. If not specified, the entries are not changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDictionaryRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "language" in value:
        import aws_sdk_elementalinference.types.dictionary_language

        out["language"] = (
            aws_sdk_elementalinference.types.dictionary_language.serialize_json(
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
        import aws_sdk_elementalinference.types.dictionary_language

        out["language"] = (
            aws_sdk_elementalinference.types.dictionary_language.deserialize_json(
                data["language"]
            )
        )
    if "entries" in data:
        out["entries"] = data["entries"]
    return out
