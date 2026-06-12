"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsJobSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.content_redaction
    import aws_sdk_transcribe.types.language_id_settings_map
    import aws_sdk_transcribe.types.language_options
    import aws_sdk_transcribe.types.model_name
    import aws_sdk_transcribe.types.summarization
    import aws_sdk_transcribe.types.vocabulary_filter_method
    import aws_sdk_transcribe.types.vocabulary_filter_name
    import aws_sdk_transcribe.types.vocabulary_name


class CallAnalyticsJobSettings(TypedDict):
    vocabulary_name: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_name.VocabularyName"
    ]
    """<p>The name of the custom vocabulary you want to include in your Call Analytics transcription request. Custom vocabulary names are case sensitive.</p>"""
    vocabulary_filter_name: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>The name of the custom vocabulary filter you want to include in your Call Analytics transcription request. Custom vocabulary filter names are case sensitive.</p> <p>Note that if you include <code>VocabularyFilterName</code> in your request, you must also include <code>VocabularyFilterMethod</code>.</p>"""
    vocabulary_filter_method: NotRequired[
        "aws_sdk_transcribe.types.vocabulary_filter_method.VocabularyFilterMethod"
    ]
    """<p>Specify how you want your custom vocabulary filter applied to your transcript.</p> <p>To replace words with <code>***</code>, choose <code>mask</code>.</p> <p>To delete words, choose <code>remove</code>.</p> <p>To flag words without changing them, choose <code>tag</code>.</p>"""
    language_model_name: NotRequired["aws_sdk_transcribe.types.model_name.ModelName"]
    """<p>The name of the custom language model you want to use when processing your Call Analytics job. Note that custom language model names are case sensitive.</p> <p>The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.</p>"""
    content_redaction: NotRequired[
        "aws_sdk_transcribe.types.content_redaction.ContentRedaction"
    ]
    language_options: NotRequired[
        "aws_sdk_transcribe.types.language_options.LanguageOptions"
    ]
    """<p>You can specify two or more language codes that represent the languages you think may be present in your media. Including more than five is not recommended. If you're unsure what languages are present, do not include this parameter.</p> <p>Including language options can improve the accuracy of language identification.</p> <p>For a list of languages supported with Call Analytics, refer to the <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html\">Supported languages</a> table.</p> <p>To transcribe speech in Modern Standard Arabic (<code>ar-SA</code>) in Amazon Web Services GovCloud (US) (US-West, us-gov-west-1), Amazon Web Services GovCloud (US) (US-East, us-gov-east-1), Canada (Calgary) ca-west-1 and Africa (Cape Town) af-south-1, your media file must be encoded at a sample rate of 16,000 Hz or higher.</p>"""
    language_id_settings: NotRequired[
        "aws_sdk_transcribe.types.language_id_settings_map.LanguageIdSettingsMap"
    ]
    """<p>If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include <code>LanguageIdSettings</code> with the relevant sub-parameters (<code>VocabularyName</code>, <code>LanguageModelName</code>, and <code>VocabularyFilterName</code>).</p> <p> <code>LanguageIdSettings</code> supports two to five language codes. Each language code you include can have an associated custom language model, custom vocabulary, and custom vocabulary filter. The language codes that you specify must match the languages of the associated custom language models, custom vocabularies, and custom vocabulary filters.</p> <p>It's recommended that you include <code>LanguageOptions</code> when using <code>LanguageIdSettings</code> to ensure that the correct language dialect is identified. For example, if you specify a custom vocabulary that is in <code>en-US</code> but Amazon Transcribe determines that the language spoken in your media is <code>en-AU</code>, your custom vocabulary <i>is not</i> applied to your transcription. If you include <code>LanguageOptions</code> and include <code>en-US</code> as the only English language dialect, your custom vocabulary <i>is</i> applied to your transcription.</p> <p>If you want to include a custom language model, custom vocabulary, or custom vocabulary filter with your request but <b>do not</b> want to use automatic language identification, use instead the <code></code> parameter with the <code>LanguageModelName</code>, <code>VocabularyName</code>, or <code>VocabularyFilterName</code> sub-parameters.</p> <p>For a list of languages supported with Call Analytics, refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html\">Supported languages and language-specific features</a>.</p>"""
    summarization: NotRequired["aws_sdk_transcribe.types.summarization.Summarization"]
    """<p>Contains <code>GenerateAbstractiveSummary</code>, which is a required parameter if you want to enable Generative call summarization in your Call Analytics request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsJobSettings) -> dict:
    out: dict = {}
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "vocabulary_filter_method" in value:
        import aws_sdk_transcribe.types.vocabulary_filter_method

        out["VocabularyFilterMethod"] = (
            aws_sdk_transcribe.types.vocabulary_filter_method.serialize_aws_json_1_1(
                value["vocabulary_filter_method"]
            )
        )
    if "language_model_name" in value:
        out["LanguageModelName"] = value["language_model_name"]
    if "content_redaction" in value:
        import aws_sdk_transcribe.types.content_redaction

        out["ContentRedaction"] = (
            aws_sdk_transcribe.types.content_redaction.serialize_aws_json_1_1(
                value["content_redaction"]
            )
        )
    if "language_options" in value:
        import aws_sdk_transcribe.types.language_options

        out["LanguageOptions"] = (
            aws_sdk_transcribe.types.language_options.serialize_aws_json_1_1(
                value["language_options"]
            )
        )
    if "language_id_settings" in value:
        import aws_sdk_transcribe.types.language_id_settings_map

        out["LanguageIdSettings"] = (
            aws_sdk_transcribe.types.language_id_settings_map.serialize_aws_json_1_1(
                value["language_id_settings"]
            )
        )
    if "summarization" in value:
        import aws_sdk_transcribe.types.summarization

        out["Summarization"] = (
            aws_sdk_transcribe.types.summarization.serialize_aws_json_1_1(
                value["summarization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CallAnalyticsJobSettings:
    out: CallAnalyticsJobSettings = {}  # type: ignore[typeddict-item]
    if "VocabularyName" in data:
        out["vocabulary_name"] = data["VocabularyName"]
    if "VocabularyFilterName" in data:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if "VocabularyFilterMethod" in data:
        import aws_sdk_transcribe.types.vocabulary_filter_method

        out["vocabulary_filter_method"] = (
            aws_sdk_transcribe.types.vocabulary_filter_method.deserialize_aws_json_1_1(
                data["VocabularyFilterMethod"]
            )
        )
    if "LanguageModelName" in data:
        out["language_model_name"] = data["LanguageModelName"]
    if "ContentRedaction" in data:
        import aws_sdk_transcribe.types.content_redaction

        out["content_redaction"] = (
            aws_sdk_transcribe.types.content_redaction.deserialize_aws_json_1_1(
                data["ContentRedaction"]
            )
        )
    if "LanguageOptions" in data:
        import aws_sdk_transcribe.types.language_options

        out["language_options"] = (
            aws_sdk_transcribe.types.language_options.deserialize_aws_json_1_1(
                data["LanguageOptions"]
            )
        )
    if "LanguageIdSettings" in data:
        import aws_sdk_transcribe.types.language_id_settings_map

        out["language_id_settings"] = (
            aws_sdk_transcribe.types.language_id_settings_map.deserialize_aws_json_1_1(
                data["LanguageIdSettings"]
            )
        )
    if "Summarization" in data:
        import aws_sdk_transcribe.types.summarization

        out["summarization"] = (
            aws_sdk_transcribe.types.summarization.deserialize_aws_json_1_1(
                data["Summarization"]
            )
        )
    return out
