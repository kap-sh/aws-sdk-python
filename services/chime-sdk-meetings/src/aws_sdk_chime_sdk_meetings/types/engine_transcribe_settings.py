"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#EngineTranscribeSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.boolean
    import aws_sdk_chime_sdk_meetings.types.string
    import aws_sdk_chime_sdk_meetings.types.transcribe_content_identification_type
    import aws_sdk_chime_sdk_meetings.types.transcribe_content_redaction_type
    import aws_sdk_chime_sdk_meetings.types.transcribe_language_code
    import aws_sdk_chime_sdk_meetings.types.transcribe_language_model_name
    import aws_sdk_chime_sdk_meetings.types.transcribe_language_options
    import aws_sdk_chime_sdk_meetings.types.transcribe_partial_results_stability
    import aws_sdk_chime_sdk_meetings.types.transcribe_pii_entity_types
    import aws_sdk_chime_sdk_meetings.types.transcribe_region
    import aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_filter_method
    import aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_names_or_filter_names_string


class EngineTranscribeSettings(TypedDict):
    language_code: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_language_code.TranscribeLanguageCode"
    ]
    """<p>Specify the language code that represents the language spoken.</p> <p>If you're unsure of the language spoken in your audio, consider using <code>IdentifyLanguage</code> to enable automatic language identification.</p>"""
    vocabulary_filter_method: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_filter_method.TranscribeVocabularyFilterMethod"
    ]
    """<p>Specify how you want your vocabulary filter applied to your transcript.</p> <p>To replace words with <code>***</code>, choose <code>mask</code>.</p> <p>To delete words, choose <code>remove</code>.</p> <p>To flag words without changing them, choose <code>tag</code>.</p>"""
    vocabulary_filter_name: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.string.String"
    ]
    """<p>Specify the name of the custom vocabulary filter that you want to use when processing your transcription. Note that vocabulary filter names are case sensitive. </p> <p>If you use Amazon Transcribe in multiple Regions, the vocabulary filter must be available in Amazon Transcribe in each Region.</p> <p>If you include <code>IdentifyLanguage</code> and want to use one or more vocabulary filters with your transcription, use the <code>VocabularyFilterNames</code> parameter instead.</p>"""
    vocabulary_name: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    """<p>Specify the name of the custom vocabulary that you want to use when processing your transcription. Note that vocabulary names are case sensitive.</p> <p>If you use Amazon Transcribe multiple Regions, the vocabulary must be available in Amazon Transcribe in each Region.</p> <p>If you include <code>IdentifyLanguage</code> and want to use one or more custom vocabularies with your transcription, use the <code>VocabularyNames</code> parameter instead.</p>"""
    region: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_region.TranscribeRegion"
    ]
    r"""<p>The Amazon Web Services Region in which to use Amazon Transcribe.</p> <p>If you don't specify a Region, then the <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html\">MediaRegion</a> of the meeting is used. However, if Amazon Transcribe is not available in the <code>MediaRegion</code>, then a <code>TranscriptFailed</code> event is sent.</p> <p>Use <code>auto</code> to use Amazon Transcribe in a Region near the meeting’s <code>MediaRegion</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/transcription-options.html#choose-region\">Choosing a transcription Region</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>"""
    enable_partial_results_stabilization: (
        "aws_sdk_chime_sdk_meetings.types.boolean.Boolean"
    )
    """<p>Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy.</p>"""
    partial_results_stability: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_partial_results_stability.TranscribePartialResultsStability"
    ]
    """<p>Specify the level of stability to use when you enable partial results stabilization (<code>EnablePartialResultsStabilization</code>).</p> <p>Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.</p>"""
    content_identification_type: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_content_identification_type.TranscribeContentIdentificationType"
    ]
    """<p>Labels all personally identifiable information (PII) identified in your transcript. If you don't include <code>PiiEntityTypes</code>, all PII is identified.</p> <note> <p>You can’t set <code>ContentIdentificationType</code> and <code>ContentRedactionType</code>.</p> </note>"""
    content_redaction_type: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_content_redaction_type.TranscribeContentRedactionType"
    ]
    """<p>Content redaction is performed at the segment level. If you don't include <code>PiiEntityTypes</code>, all PII is redacted.</p> <note> <p>You can’t set <code>ContentRedactionType</code> and <code>ContentIdentificationType</code>.</p> </note>"""
    pii_entity_types: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_pii_entity_types.TranscribePiiEntityTypes"
    ]
    """<p>Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as you'd like, or you can select <code>ALL</code>.</p> <p>Values must be comma-separated and can include: <code>ADDRESS</code>, <code>BANK_ACCOUNT_NUMBER</code>, <code>BANK_ROUTING</code>, <code>CREDIT_DEBIT_CVV</code>, <code>CREDIT_DEBIT_EXPIRY</code> <code>CREDIT_DEBIT_NUMBER</code>, <code>EMAIL</code>,<code>NAME</code>, <code>PHONE</code>, <code>PIN</code>, <code>SSN</code>, or <code>ALL</code>.</p> <p>Note that if you include <code>PiiEntityTypes</code>, you must also include <code>ContentIdentificationType</code> or <code>ContentRedactionType</code>.</p> <p>If you include <code>ContentRedactionType</code> or <code>ContentIdentificationType</code>, but do not include PiiEntityTypes, all PII is redacted or identified.</p>"""
    language_model_name: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_language_model_name.TranscribeLanguageModelName"
    ]
    """<p>Specify the name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.</p> <p>The language of the specified language model must match the language code. If the languages don't match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.</p> <p>If you use Amazon Transcribe in multiple Regions, the custom language model must be available in Amazon Transcribe in each Region.</p>"""
    identify_language: "aws_sdk_chime_sdk_meetings.types.boolean.Boolean"
    """<p>Enables automatic language identification for your transcription.</p> <p>If you include <code>IdentifyLanguage</code>, you can optionally use <code>LanguageOptions</code> to include a list of language codes that you think may be present in your audio stream. Including language options can improve transcription accuracy.</p> <p>You can also use <code>PreferredLanguage</code> to include a preferred language. Doing so can help Amazon Transcribe identify the language faster.</p> <p>You must include either <code>LanguageCode</code> or <code>IdentifyLanguage</code>.</p> <p>Language identification can't be combined with custom language models or redaction.</p>"""
    language_options: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_language_options.TranscribeLanguageOptions"
    ]
    """<p>Specify two or more language codes that represent the languages you think may be present in your media; including more than five is not recommended. If you're unsure what languages are present, do not include this parameter.</p> <p>Including language options can improve the accuracy of language identification.</p> <p>If you include <code>LanguageOptions</code>, you must also include <code>IdentifyLanguage</code>.</p> <important> <p>You can only include one language dialect per language. For example, you cannot include <code>en-US</code> and <code>en-AU</code>.</p> </important>"""
    preferred_language: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_language_code.TranscribeLanguageCode"
    ]
    """<p>Specify a preferred language from the subset of languages codes you specified in <code>LanguageOptions</code>.</p> <p>You can only use this parameter if you include <code>IdentifyLanguage</code> and <code>LanguageOptions</code>.</p>"""
    vocabulary_names: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_names_or_filter_names_string.TranscribeVocabularyNamesOrFilterNamesString"
    ]
    """<p>Specify the names of the custom vocabularies that you want to use when processing your transcription. Note that vocabulary names are case sensitive.</p> <p>If you use Amazon Transcribe in multiple Regions, the vocabulary must be available in Amazon Transcribe in each Region.</p> <p>If you don't include <code>IdentifyLanguage</code> and want to use a custom vocabulary with your transcription, use the <code>VocabularyName</code> parameter instead.</p>"""
    vocabulary_filter_names: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_names_or_filter_names_string.TranscribeVocabularyNamesOrFilterNamesString"
    ]
    """<p>Specify the names of the custom vocabulary filters that you want to use when processing your transcription. Note that vocabulary filter names are case sensitive.</p> <p>If you use Amazon Transcribe in multiple Regions, the vocabulary filter must be available in Amazon Transcribe in each Region.</p> <p> If you're <i>not</i> including <code>IdentifyLanguage</code> and want to use a custom vocabulary filter with your transcription, use the <code>VocabularyFilterName</code> parameter instead.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngineTranscribeSettings) -> dict:
    out: dict = {}
    if "language_code" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_language_code

        out["LanguageCode"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "vocabulary_filter_method" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_filter_method

        out["VocabularyFilterMethod"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_filter_method.serialize_json(
                value["vocabulary_filter_method"]
            )
        )
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "region" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_region

        out["Region"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_region.serialize_json(
                value["region"]
            )
        )
    out["EnablePartialResultsStabilization"] = value.get(
        "enable_partial_results_stabilization", False
    )
    if "partial_results_stability" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_partial_results_stability

        out["PartialResultsStability"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_partial_results_stability.serialize_json(
                value["partial_results_stability"]
            )
        )
    if "content_identification_type" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_content_identification_type

        out["ContentIdentificationType"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_content_identification_type.serialize_json(
                value["content_identification_type"]
            )
        )
    if "content_redaction_type" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_content_redaction_type

        out["ContentRedactionType"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_content_redaction_type.serialize_json(
                value["content_redaction_type"]
            )
        )
    if "pii_entity_types" in value:
        out["PiiEntityTypes"] = value["pii_entity_types"]
    if "language_model_name" in value:
        out["LanguageModelName"] = value["language_model_name"]
    out["IdentifyLanguage"] = value.get("identify_language", False)
    if "language_options" in value:
        out["LanguageOptions"] = value["language_options"]
    if "preferred_language" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_language_code

        out["PreferredLanguage"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_language_code.serialize_json(
                value["preferred_language"]
            )
        )
    if "vocabulary_names" in value:
        out["VocabularyNames"] = value["vocabulary_names"]
    if "vocabulary_filter_names" in value:
        out["VocabularyFilterNames"] = value["vocabulary_filter_names"]
    return out


def deserialize_json(data: dict) -> EngineTranscribeSettings:
    out: EngineTranscribeSettings = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_language_code

        out["language_code"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if "VocabularyFilterMethod" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_filter_method

        out["vocabulary_filter_method"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_vocabulary_filter_method.deserialize_json(
                data["VocabularyFilterMethod"]
            )
        )
    if "VocabularyFilterName" in data:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if "VocabularyName" in data:
        out["vocabulary_name"] = data["VocabularyName"]
    if "Region" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_region

        out["region"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_region.deserialize_json(
                data["Region"]
            )
        )
    if "EnablePartialResultsStabilization" in data:
        out["enable_partial_results_stabilization"] = data[
            "EnablePartialResultsStabilization"
        ]
    else:
        out["enable_partial_results_stabilization"] = False
    if "PartialResultsStability" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_partial_results_stability

        out["partial_results_stability"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_partial_results_stability.deserialize_json(
                data["PartialResultsStability"]
            )
        )
    if "ContentIdentificationType" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_content_identification_type

        out["content_identification_type"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_content_identification_type.deserialize_json(
                data["ContentIdentificationType"]
            )
        )
    if "ContentRedactionType" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_content_redaction_type

        out["content_redaction_type"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_content_redaction_type.deserialize_json(
                data["ContentRedactionType"]
            )
        )
    if "PiiEntityTypes" in data:
        out["pii_entity_types"] = data["PiiEntityTypes"]
    if "LanguageModelName" in data:
        out["language_model_name"] = data["LanguageModelName"]
    if "IdentifyLanguage" in data:
        out["identify_language"] = data["IdentifyLanguage"]
    else:
        out["identify_language"] = False
    if "LanguageOptions" in data:
        out["language_options"] = data["LanguageOptions"]
    if "PreferredLanguage" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_language_code

        out["preferred_language"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_language_code.deserialize_json(
                data["PreferredLanguage"]
            )
        )
    if "VocabularyNames" in data:
        out["vocabulary_names"] = data["VocabularyNames"]
    if "VocabularyFilterNames" in data:
        out["vocabulary_filter_names"] = data["VocabularyFilterNames"]
    return out
