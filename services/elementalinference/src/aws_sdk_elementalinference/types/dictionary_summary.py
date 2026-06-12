"""Generated from Smithy shape ``com.amazonaws.elementalinference#DictionarySummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.dictionary_arn
    import aws_sdk_elementalinference.types.dictionary_id
    import aws_sdk_elementalinference.types.dictionary_language
    import aws_sdk_elementalinference.types.dictionary_status
    import aws_sdk_elementalinference.types.resource_name


class DictionarySummary(TypedDict):
    arn: "aws_sdk_elementalinference.types.dictionary_arn.DictionaryArn"
    """<p>The ARN of the dictionary.</p>"""
    id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary.</p>"""
    name: "aws_sdk_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the dictionary.</p>"""
    language: "aws_sdk_elementalinference.types.dictionary_language.DictionaryLanguage"
    """<p>The language of the dictionary.</p>"""
    status: "aws_sdk_elementalinference.types.dictionary_status.DictionaryStatus"
    """<p>The status of the dictionary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DictionarySummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_elementalinference.types.dictionary_language

    out["language"] = (
        aws_sdk_elementalinference.types.dictionary_language.serialize_json(
            value["language"]
        )
    )
    import aws_sdk_elementalinference.types.dictionary_status

    out["status"] = aws_sdk_elementalinference.types.dictionary_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DictionarySummary:
    out: DictionarySummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DictionarySummary.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DictionarySummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DictionarySummary.name required")
    if "language" in data:
        import aws_sdk_elementalinference.types.dictionary_language

        out["language"] = (
            aws_sdk_elementalinference.types.dictionary_language.deserialize_json(
                data["language"]
            )
        )
    else:
        raise DeserializationError("DictionarySummary.language required")
    if "status" in data:
        import aws_sdk_elementalinference.types.dictionary_status

        out["status"] = (
            aws_sdk_elementalinference.types.dictionary_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DictionarySummary.status required")
    return out
