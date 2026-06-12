"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalScribeStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_scribe_language_code
    import aws_sdk_transcribe_streaming.types.medical_scribe_media_encoding
    import aws_sdk_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz
    import aws_sdk_transcribe_streaming.types.medical_scribe_result_stream
    import aws_sdk_transcribe_streaming.types.request_id
    import aws_sdk_transcribe_streaming.types.session_id


class StartMedicalScribeStreamResponse(TypedDict):
    session_id: NotRequired["aws_sdk_transcribe_streaming.types.session_id.SessionId"]
    """<p>The identifier (in UUID format) for your streaming session.</p> <p>If you already started streaming, this is same ID as the one you specified in your initial <code>StartMedicalScribeStreamRequest</code>. </p>"""
    request_id: NotRequired["aws_sdk_transcribe_streaming.types.request_id.RequestId"]
    """<p>The unique identifier for your streaming request. </p>"""
    language_code: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The Language Code that you specified in your request. Same as provided in the <code>StartMedicalScribeStreamRequest</code>. </p>"""
    media_sample_rate_hertz: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    ]
    """<p>The sample rate (in hertz) that you specified in your request. Same as provided in the <code>StartMedicalScribeStreamRequest</code> </p>"""
    media_encoding: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    ]
    """<p>The Media Encoding you specified in your request. Same as provided in the <code>StartMedicalScribeStreamRequest</code> </p>"""
    result_stream: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_result_stream.MedicalScribeResultStream"
    ]
    """<p>The result stream where you will receive the output events. </p>"""
