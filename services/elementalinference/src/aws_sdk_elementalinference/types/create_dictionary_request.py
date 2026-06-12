"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateDictionaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_entries_payload
    import aws_sdk_elementalinference.types.dictionary_language
    import aws_sdk_elementalinference.types.resource_name
    import aws_sdk_elementalinference.types.tag_map


class CreateDictionaryRequest(TypedDict):
    name: "aws_sdk_elementalinference.types.resource_name.ResourceName"
    """<p>A user-friendly name for this dictionary.</p>"""
    language: "aws_sdk_elementalinference.types.dictionary_language.DictionaryLanguage"
    """<p>The language of the dictionary entries. Specify the language using an ISO 639-2/T three-letter code. Supported values: eng, fra, ita, deu, spa, por. </p>"""
    entries: NotRequired[
        "aws_sdk_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
    ]
    """<p>The dictionary entries payload. Contains the custom words and phrases for the dictionary. Maximum size is 40,960 characters. </p>"""
    tags: NotRequired["aws_sdk_elementalinference.types.tag_map.TagMap"]
    """<p>Optional tags to associate with the dictionary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDictionaryRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_elementalinference.types.dictionary_language

    out["language"] = (
        aws_sdk_elementalinference.types.dictionary_language.serialize_json(
            value["language"]
        )
    )
    if "entries" in value:
        out["entries"] = value["entries"]
    if "tags" in value:
        import aws_sdk_elementalinference.types.tag_map

        out["tags"] = aws_sdk_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDictionaryRequest:
    out: CreateDictionaryRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDictionaryRequest.name required")
    if "language" in data:
        import aws_sdk_elementalinference.types.dictionary_language

        out["language"] = (
            aws_sdk_elementalinference.types.dictionary_language.deserialize_json(
                data["language"]
            )
        )
    else:
        raise DeserializationError("CreateDictionaryRequest.language required")
    if "entries" in data:
        out["entries"] = data["entries"]
    if "tags" in data:
        import aws_sdk_elementalinference.types.tag_map

        out["tags"] = aws_sdk_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
