"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetDictionaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.dictionary_arn
    import capo_elementalinference.types.dictionary_id
    import capo_elementalinference.types.dictionary_language
    import capo_elementalinference.types.dictionary_status
    import capo_elementalinference.types.feed_references
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map


class GetDictionaryResponse(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the dictionary.</p>"""
    arn: "capo_elementalinference.types.dictionary_arn.DictionaryArn"
    """<p>The ARN of the dictionary.</p>"""
    id: "capo_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary.</p>"""
    language: "capo_elementalinference.types.dictionary_language.DictionaryLanguage"
    """<p>The language of the dictionary.</p>"""
    status: "capo_elementalinference.types.dictionary_status.DictionaryStatus"
    """<p>The current status of the dictionary.</p>"""
    references: NotRequired[
        "capo_elementalinference.types.feed_references.FeedReferences"
    ]
    """<p>A list of feed IDs that reference this dictionary.</p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>The tags associated with the dictionary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDictionaryResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_elementalinference.types.dictionary_language

    out["language"] = capo_elementalinference.types.dictionary_language.serialize_json(
        value["language"]
    )
    import capo_elementalinference.types.dictionary_status

    out["status"] = capo_elementalinference.types.dictionary_status.serialize_json(
        value["status"]
    )
    if "references" in value:
        import capo_elementalinference.types.feed_references

        out["references"] = (
            capo_elementalinference.types.feed_references.serialize_json(
                value["references"]
            )
        )
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetDictionaryResponse:
    out: GetDictionaryResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetDictionaryResponse.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetDictionaryResponse.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetDictionaryResponse.id required")
    if "language" in data:
        import capo_elementalinference.types.dictionary_language

        out["language"] = (
            capo_elementalinference.types.dictionary_language.deserialize_json(
                data["language"]
            )
        )
    else:
        raise DeserializationError("GetDictionaryResponse.language required")
    if "status" in data:
        import capo_elementalinference.types.dictionary_status

        out["status"] = (
            capo_elementalinference.types.dictionary_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetDictionaryResponse.status required")
    if "references" in data:
        import capo_elementalinference.types.feed_references

        out["references"] = (
            capo_elementalinference.types.feed_references.deserialize_json(
                data["references"]
            )
        )
    if "tags" in data:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
