"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateMedicalVocabularyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.failure_reason
    import aws_sdk_transcribe.types.language_code
    import aws_sdk_transcribe.types.vocabulary_name
    import aws_sdk_transcribe.types.vocabulary_state


class CreateMedicalVocabularyResponse(TypedDict, closed=True):
    vocabulary_name: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_name.VocabularyName"
    ]
    """<p>The name you chose for your custom medical vocabulary.</p>"""
    language_code: NotRequired["aws_sdk_transcribe.types.language_code.LanguageCode"]
    """<p>The language code you selected for your custom medical vocabulary. US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p>"""
    vocabulary_state: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_state.VocabularyState"
    ]
    """<p>The processing state of your custom medical vocabulary. If the state is <code>READY</code>, you can use the custom vocabulary in a <code>StartMedicalTranscriptionJob</code> request.</p>"""
    last_modified_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time you created your custom medical vocabulary.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    failure_reason: NotRequired["aws_sdk_transcribe.types.failure_reason.FailureReason"]
    r"""<p>If <code>VocabularyState</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the medical transcription job request failed. See also: <a href=\"https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html\">Common Errors</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMedicalVocabularyResponse) -> dict:
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
    if "vocabulary_state" in value:
        import aws_sdk_transcribe.types.vocabulary_state

        out["VocabularyState"] = (
            aws_sdk_transcribe.types.vocabulary_state.serialize_aws_json_1_1(
                value["vocabulary_state"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["LastModifiedTime"] = (
            aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMedicalVocabularyResponse:
    out: CreateMedicalVocabularyResponse = {}  # type: ignore[typeddict-item]
    if "VocabularyName" in data:
        out["vocabulary_name"] = data["VocabularyName"]
    if "LanguageCode" in data:
        import aws_sdk_transcribe.types.language_code

        out["language_code"] = (
            aws_sdk_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "VocabularyState" in data:
        import aws_sdk_transcribe.types.vocabulary_state

        out["vocabulary_state"] = (
            aws_sdk_transcribe.types.vocabulary_state.deserialize_aws_json_1_1(
                data["VocabularyState"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["last_modified_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
