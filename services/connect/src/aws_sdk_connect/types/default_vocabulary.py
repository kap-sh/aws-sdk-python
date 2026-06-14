"""Generated from Smithy shape ``com.amazonaws.connect#DefaultVocabulary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.vocabulary_id
    import aws_sdk_connect.types.vocabulary_language_code
    import aws_sdk_connect.types.vocabulary_name


class DefaultVocabulary(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    language_code: (
        "aws_sdk_connect.types.vocabulary_language_code.VocabularyLanguageCode"
    )
    r"""<p>The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html\">What is Amazon Transcribe?</a> </p>"""
    vocabulary_id: "aws_sdk_connect.types.vocabulary_id.VocabularyId"
    """<p>The identifier of the custom vocabulary.</p>"""
    vocabulary_name: "aws_sdk_connect.types.vocabulary_name.VocabularyName"
    """<p>A unique name of the custom vocabulary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultVocabulary) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import aws_sdk_connect.types.vocabulary_language_code

    out["LanguageCode"] = aws_sdk_connect.types.vocabulary_language_code.serialize_json(
        value["language_code"]
    )
    out["VocabularyId"] = value["vocabulary_id"]
    out["VocabularyName"] = value["vocabulary_name"]
    return out


def deserialize_json(data: dict) -> DefaultVocabulary:
    out: DefaultVocabulary = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("DefaultVocabulary.instance_id required")
    if "LanguageCode" in data:
        import aws_sdk_connect.types.vocabulary_language_code

        out["language_code"] = (
            aws_sdk_connect.types.vocabulary_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("DefaultVocabulary.language_code required")
    if "VocabularyId" in data:
        out["vocabulary_id"] = data["VocabularyId"]
    else:
        raise DeserializationError("DefaultVocabulary.vocabulary_id required")
    if "VocabularyName" in data:
        out["vocabulary_name"] = data["VocabularyName"]
    else:
        raise DeserializationError("DefaultVocabulary.vocabulary_name required")
    return out
