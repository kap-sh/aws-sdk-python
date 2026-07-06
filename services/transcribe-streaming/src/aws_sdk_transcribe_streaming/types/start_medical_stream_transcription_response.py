"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalStreamTranscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.boolean
    import aws_sdk_transcribe_streaming.types.language_code
    import aws_sdk_transcribe_streaming.types.media_encoding
    import aws_sdk_transcribe_streaming.types.media_sample_rate_hertz
    import aws_sdk_transcribe_streaming.types.medical_content_identification_type
    import aws_sdk_transcribe_streaming.types.medical_transcript_result_stream
    import aws_sdk_transcribe_streaming.types.number_of_channels
    import aws_sdk_transcribe_streaming.types.request_id
    import aws_sdk_transcribe_streaming.types.session_id
    import aws_sdk_transcribe_streaming.types.specialty
    import aws_sdk_transcribe_streaming.types.type
    import aws_sdk_transcribe_streaming.types.vocabulary_name


class StartMedicalStreamTranscriptionResponse(TypedDict, closed=True):
    request_id: NotRequired["aws_sdk_transcribe_streaming.types.request_id.RequestId"]
    """<p>Provides the identifier for your streaming request.</p>"""
    language_code: NotRequired[
        "aws_sdk_transcribe_streaming.types.language_code.LanguageCode"
    ]
    """<p>Provides the language code that you specified in your request. This must be <code>en-US</code>.</p>"""
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
    specialty: NotRequired["aws_sdk_transcribe_streaming.types.specialty.Specialty"]
    """<p>Provides the medical specialty that you specified in your request.</p>"""
    type: NotRequired["aws_sdk_transcribe_streaming.types.type.Type"]
    """<p>Provides the type of audio you specified in your request.</p>"""
    show_speaker_label: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Shows whether speaker partitioning was enabled for your transcription.</p>"""
    session_id: NotRequired["aws_sdk_transcribe_streaming.types.session_id.SessionId"]
    """<p>Provides the identifier for your transcription session.</p>"""
    transcript_result_stream: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_transcript_result_stream.MedicalTranscriptResultStream"
    ]
    """<p>Provides detailed information about your streaming session.</p>"""
    enable_channel_identification: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Shows whether channel identification was enabled for your transcription.</p>"""
    number_of_channels: NotRequired[
        "aws_sdk_transcribe_streaming.types.number_of_channels.NumberOfChannels"
    ]
    """<p>Provides the number of channels that you specified in your request.</p>"""
    content_identification_type: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_content_identification_type.MedicalContentIdentificationType"
    ]
    """<p>Shows whether content identification was enabled for your transcription.</p>"""
