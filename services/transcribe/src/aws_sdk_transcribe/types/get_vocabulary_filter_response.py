"""Generated from Smithy shape ``com.amazonaws.transcribe#GetVocabularyFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.language_code
    import aws_sdk_transcribe.types.uri
    import aws_sdk_transcribe.types.vocabulary_filter_name


class GetVocabularyFilterResponse(TypedDict, closed=True):
    vocabulary_filter_name: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>The name of the custom vocabulary filter you requested information about.</p>"""
    language_code: NotRequired["aws_sdk_transcribe.types.language_code.LanguageCode"]
    """<p>The language code you selected for your custom vocabulary filter.</p>"""
    last_modified_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom vocabulary filter was last modified.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    download_uri: NotRequired["aws_sdk_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location where the custom vocabulary filter is stored; use this URI to view or download the custom vocabulary filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetVocabularyFilterResponse) -> dict:
    out: dict = {}
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
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
    if "download_uri" in value:
        out["DownloadUri"] = value["download_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetVocabularyFilterResponse:
    out: GetVocabularyFilterResponse = {}  # type: ignore[typeddict-item]
    if "VocabularyFilterName" in data:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
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
    if "DownloadUri" in data:
        out["download_uri"] = data["DownloadUri"]
    return out
