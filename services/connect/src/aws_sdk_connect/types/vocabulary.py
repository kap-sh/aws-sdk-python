"""Generated from Smithy shape ``com.amazonaws.connect#Vocabulary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.vocabulary_content
    import aws_sdk_connect.types.vocabulary_failure_reason
    import aws_sdk_connect.types.vocabulary_id
    import aws_sdk_connect.types.vocabulary_language_code
    import aws_sdk_connect.types.vocabulary_last_modified_time
    import aws_sdk_connect.types.vocabulary_name
    import aws_sdk_connect.types.vocabulary_state


class Vocabulary(TypedDict):
    name: "aws_sdk_connect.types.vocabulary_name.VocabularyName"
    """<p>A unique name of the custom vocabulary.</p>"""
    id: "aws_sdk_connect.types.vocabulary_id.VocabularyId"
    """<p>The identifier of the custom vocabulary.</p>"""
    arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the custom vocabulary.</p>"""
    language_code: (
        "aws_sdk_connect.types.vocabulary_language_code.VocabularyLanguageCode"
    )
    r"""<p>The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html\">What is Amazon Transcribe?</a> </p>"""
    state: "aws_sdk_connect.types.vocabulary_state.VocabularyState"
    """<p>The current state of the custom vocabulary.</p>"""
    last_modified_time: (
        "aws_sdk_connect.types.vocabulary_last_modified_time.VocabularyLastModifiedTime"
    )
    """<p>The timestamp when the custom vocabulary was last modified.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_connect.types.vocabulary_failure_reason.VocabularyFailureReason"
    ]
    """<p>The reason why the custom vocabulary was not created.</p>"""
    content: NotRequired["aws_sdk_connect.types.vocabulary_content.VocabularyContent"]
    r"""<p>The content of the custom vocabulary in plain-text format with a table of values. Each row in the table represents a word or a phrase, described with <code>Phrase</code>, <code>IPA</code>, <code>SoundsLike</code>, and <code>DisplayAs</code> fields. Separate the fields with TAB characters. For more information, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html#create-vocabulary-table\">Create a custom vocabulary using a table</a>.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Vocabulary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import aws_sdk_connect.types.vocabulary_language_code

    out["LanguageCode"] = aws_sdk_connect.types.vocabulary_language_code.serialize_json(
        value["language_code"]
    )
    import aws_sdk_connect.types.vocabulary_state

    out["State"] = aws_sdk_connect.types.vocabulary_state.serialize_json(value["state"])
    import aws_sdk_connect.types.vocabulary_last_modified_time

    out["LastModifiedTime"] = (
        aws_sdk_connect.types.vocabulary_last_modified_time.serialize_json(
            value["last_modified_time"]
        )
    )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "content" in value:
        out["Content"] = value["content"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Vocabulary:
    out: Vocabulary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Vocabulary.name required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Vocabulary.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Vocabulary.arn required")
    if "LanguageCode" in data:
        import aws_sdk_connect.types.vocabulary_language_code

        out["language_code"] = (
            aws_sdk_connect.types.vocabulary_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("Vocabulary.language_code required")
    if "State" in data:
        import aws_sdk_connect.types.vocabulary_state

        out["state"] = aws_sdk_connect.types.vocabulary_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("Vocabulary.state required")
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.vocabulary_last_modified_time

        out["last_modified_time"] = (
            aws_sdk_connect.types.vocabulary_last_modified_time.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("Vocabulary.last_modified_time required")
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
