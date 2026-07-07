"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalScribeListeningSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.medical_scribe_input_stream
    import aws_sdk_connecthealth.types.medical_scribe_language_code
    import aws_sdk_connecthealth.types.medical_scribe_media_encoding
    import aws_sdk_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import aws_sdk_connecthealth.types.scribe_session_id
    import aws_sdk_connecthealth.types.subscription_id


class StartMedicalScribeListeningSessionInput(TypedDict, closed=True):
    session_id: "aws_sdk_connecthealth.types.scribe_session_id.ScribeSessionId"
    """<p>The Session identifier</p>"""
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p>The Domain identifier</p>"""
    subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId"
    """<p>The Subscription identifier</p>"""
    language_code: "aws_sdk_connecthealth.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    """<p>The Language Code for the audio in the session</p>"""
    media_sample_rate_hertz: "aws_sdk_connecthealth.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    """<p>The sample rate of the input audio</p>"""
    media_encoding: "aws_sdk_connecthealth.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    """<p>The encoding for the input audio</p>"""
    input_stream: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_input_stream.MedicalScribeInputStream"
    ]
    """<p/>"""
