"""Generated from Smithy shape ``com.amazonaws.connect#VocabularySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.vocabulary_failure_reason
    import aws_sdk_connect.types.vocabulary_id
    import aws_sdk_connect.types.vocabulary_language_code
    import aws_sdk_connect.types.vocabulary_last_modified_time
    import aws_sdk_connect.types.vocabulary_name
    import aws_sdk_connect.types.vocabulary_state


class VocabularySummary(TypedDict):
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


# --- restJson1 ser/de ---
def serialize_json(value: VocabularySummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> VocabularySummary:
    out: VocabularySummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("VocabularySummary.name required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("VocabularySummary.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("VocabularySummary.arn required")
    if "LanguageCode" in data:
        import aws_sdk_connect.types.vocabulary_language_code

        out["language_code"] = (
            aws_sdk_connect.types.vocabulary_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("VocabularySummary.language_code required")
    if "State" in data:
        import aws_sdk_connect.types.vocabulary_state

        out["state"] = aws_sdk_connect.types.vocabulary_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("VocabularySummary.state required")
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.vocabulary_last_modified_time

        out["last_modified_time"] = (
            aws_sdk_connect.types.vocabulary_last_modified_time.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("VocabularySummary.last_modified_time required")
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
