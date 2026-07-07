"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartStreamTranscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.boolean
    import aws_sdk_transcribe_streaming.types.content_identification_type
    import aws_sdk_transcribe_streaming.types.content_redaction_type
    import aws_sdk_transcribe_streaming.types.language_code
    import aws_sdk_transcribe_streaming.types.language_options
    import aws_sdk_transcribe_streaming.types.media_encoding
    import aws_sdk_transcribe_streaming.types.media_sample_rate_hertz
    import aws_sdk_transcribe_streaming.types.model_name
    import aws_sdk_transcribe_streaming.types.number_of_channels
    import aws_sdk_transcribe_streaming.types.partial_results_stability
    import aws_sdk_transcribe_streaming.types.pii_entity_types
    import aws_sdk_transcribe_streaming.types.request_id
    import aws_sdk_transcribe_streaming.types.session_id
    import aws_sdk_transcribe_streaming.types.session_resume_window
    import aws_sdk_transcribe_streaming.types.transcript_result_stream
    import aws_sdk_transcribe_streaming.types.vocabulary_filter_method
    import aws_sdk_transcribe_streaming.types.vocabulary_filter_name
    import aws_sdk_transcribe_streaming.types.vocabulary_filter_names
    import aws_sdk_transcribe_streaming.types.vocabulary_name
    import aws_sdk_transcribe_streaming.types.vocabulary_names


class StartStreamTranscriptionResponse(TypedDict, closed=True):
    request_id: NotRequired["aws_sdk_transcribe_streaming.types.request_id.RequestId"]
    """<p>Provides the identifier for your streaming request.</p>"""
    language_code: NotRequired[
        "aws_sdk_transcribe_streaming.types.language_code.LanguageCode"
    ]
    """<p>Provides the language code that you specified in your request.</p>"""
    media_sample_rate_hertz: NotRequired[
        "aws_sdk_transcribe_streaming.types.media_sample_rate_hertz.MediaSampleRateHertz"
    ]
    """<p>Provides the sample rate that you specified in your request.</p>"""
    media_encoding: NotRequired[
        "aws_sdk_transcribe_streaming.types.media_encoding.MediaEncoding"
    ]
    """<p>Provides the media encoding you specified in your request.</p>"""
    vocabulary_name: NotRequired[
        "aws_sdk_transcribe_streaming.types.vocabulary_name.VocabularyName"
    ]
    """<p>Provides the name of the custom vocabulary that you specified in your request.</p>"""
    session_id: NotRequired["aws_sdk_transcribe_streaming.types.session_id.SessionId"]
    """<p>Provides the identifier for your transcription session.</p>"""
    transcript_result_stream: NotRequired[
        "aws_sdk_transcribe_streaming.types.transcript_result_stream.TranscriptResultStream"
    ]
    """<p>Provides detailed information about your streaming session.</p>"""
    vocabulary_filter_name: NotRequired[
        "aws_sdk_transcribe_streaming.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>Provides the name of the custom vocabulary filter that you specified in your request.</p>"""
    vocabulary_filter_method: NotRequired[
        "aws_sdk_transcribe_streaming.types.vocabulary_filter_method.VocabularyFilterMethod"
    ]
    """<p>Provides the vocabulary filtering method used in your transcription.</p>"""
    show_speaker_label: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Shows whether speaker partitioning was enabled for your transcription.</p>"""
    enable_channel_identification: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Shows whether channel identification was enabled for your transcription.</p>"""
    number_of_channels: NotRequired[
        "aws_sdk_transcribe_streaming.types.number_of_channels.NumberOfChannels"
    ]
    """<p>Provides the number of channels that you specified in your request.</p>"""
    enable_partial_results_stabilization: (
        "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    )
    """<p>Shows whether partial results stabilization was enabled for your transcription.</p>"""
    partial_results_stability: NotRequired[
        "aws_sdk_transcribe_streaming.types.partial_results_stability.PartialResultsStability"
    ]
    """<p>Provides the stabilization level used for your transcription.</p>"""
    content_identification_type: NotRequired[
        "aws_sdk_transcribe_streaming.types.content_identification_type.ContentIdentificationType"
    ]
    """<p>Shows whether content identification was enabled for your transcription.</p>"""
    content_redaction_type: NotRequired[
        "aws_sdk_transcribe_streaming.types.content_redaction_type.ContentRedactionType"
    ]
    """<p>Shows whether content redaction was enabled for your transcription.</p>"""
    pii_entity_types: NotRequired[
        "aws_sdk_transcribe_streaming.types.pii_entity_types.PiiEntityTypes"
    ]
    """<p>Lists the PII entity types you specified in your request.</p>"""
    language_model_name: NotRequired[
        "aws_sdk_transcribe_streaming.types.model_name.ModelName"
    ]
    """<p>Provides the name of the custom language model that you specified in your request.</p>"""
    identify_language: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Shows whether automatic language identification was enabled for your transcription.</p>"""
    language_options: NotRequired[
        "aws_sdk_transcribe_streaming.types.language_options.LanguageOptions"
    ]
    """<p>Provides the language codes that you specified in your request.</p>"""
    preferred_language: NotRequired[
        "aws_sdk_transcribe_streaming.types.language_code.LanguageCode"
    ]
    """<p>Provides the preferred language that you specified in your request.</p>"""
    identify_multiple_languages: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Shows whether automatic multi-language identification was enabled for your transcription.</p>"""
    vocabulary_names: NotRequired[
        "aws_sdk_transcribe_streaming.types.vocabulary_names.VocabularyNames"
    ]
    """<p>Provides the names of the custom vocabularies that you specified in your request.</p>"""
    vocabulary_filter_names: NotRequired[
        "aws_sdk_transcribe_streaming.types.vocabulary_filter_names.VocabularyFilterNames"
    ]
    """<p>Provides the names of the custom vocabulary filters that you specified in your request.</p>"""
    session_resume_window: NotRequired[
        "aws_sdk_transcribe_streaming.types.session_resume_window.SessionResumeWindow"
    ]
    """<p>Provides the session resume window, in minutes, that you specified in your request.</p>"""
