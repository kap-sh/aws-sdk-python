"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateVocabularyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.language_code
    import aws_sdk_transcribe.types.vocabulary_name
    import aws_sdk_transcribe.types.vocabulary_state


class UpdateVocabularyResponse(TypedDict):
    vocabulary_name: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_name.VocabularyName"
    ]
    """<p>The name of the updated custom vocabulary.</p>"""
    language_code: NotRequired["aws_sdk_transcribe.types.language_code.LanguageCode"]
    """<p>The language code you selected for your custom vocabulary.</p>"""
    last_modified_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom vocabulary was last updated.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    vocabulary_state: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_state.VocabularyState"
    ]
    """<p>The processing state of your custom vocabulary. If the state is <code>READY</code>, you can use the custom vocabulary in a <code>StartTranscriptionJob</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVocabularyResponse) -> dict:
    out: dict = {}
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "language_code" in value:
        import aws_sdk_transcribe.types.language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["LastModifiedTime"] = (
            aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "vocabulary_state" in value:
        import aws_sdk_transcribe.types.vocabulary_state

        out["VocabularyState"] = (
            aws_sdk_transcribe.types.vocabulary_state.serialize_aws_json_1_1(
                value["vocabulary_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVocabularyResponse:
    out: UpdateVocabularyResponse = {}  # type: ignore[typeddict-item]
    if "VocabularyName" in data:
        out["vocabulary_name"] = data["VocabularyName"]
    if "LanguageCode" in data:
        import aws_sdk_transcribe.types.language_code

        out["language_code"] = (
            aws_sdk_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["last_modified_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "VocabularyState" in data:
        import aws_sdk_transcribe.types.vocabulary_state

        out["vocabulary_state"] = (
            aws_sdk_transcribe.types.vocabulary_state.deserialize_aws_json_1_1(
                data["VocabularyState"]
            )
        )
    return out
