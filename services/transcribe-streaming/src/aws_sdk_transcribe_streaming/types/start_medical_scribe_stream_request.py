"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartMedicalScribeStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_scribe_input_stream
    import aws_sdk_transcribe_streaming.types.medical_scribe_language_code
    import aws_sdk_transcribe_streaming.types.medical_scribe_media_encoding
    import aws_sdk_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz
    import aws_sdk_transcribe_streaming.types.session_id


class StartMedicalScribeStreamRequest(TypedDict):
    session_id: NotRequired["aws_sdk_transcribe_streaming.types.session_id.SessionId"]
    """<p>Specify an identifier for your streaming session (in UUID format). If you don't include a SessionId in your request, Amazon Web Services HealthScribe generates an ID and returns it in the response. </p>"""
    language_code: "aws_sdk_transcribe_streaming.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    """<p>Specify the language code for your HealthScribe streaming session.</p>"""
    media_sample_rate_hertz: "aws_sdk_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    """<p>Specify the sample rate of the input audio (in hertz). Amazon Web Services HealthScribe supports a range from 16,000 Hz to 48,000 Hz. The sample rate you specify must match that of your audio. </p>"""
    media_encoding: "aws_sdk_transcribe_streaming.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    """<p>Specify the encoding used for the input audio.</p> <p>Supported formats are:</p> <ul> <li> <p>FLAC</p> </li> <li> <p>OPUS-encoded audio in an Ogg container</p> </li> <li> <p>PCM (only signed 16-bit little-endian audio formats, which does not include WAV) </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio\">Media formats</a>. </p>"""
    input_stream: "aws_sdk_transcribe_streaming.types.medical_scribe_input_stream.MedicalScribeInputStream"
    """<p>Specify the input stream where you will send events in real time.</p> <p>The first element of the input stream must be a <code>MedicalScribeConfigurationEvent</code>. </p>"""
