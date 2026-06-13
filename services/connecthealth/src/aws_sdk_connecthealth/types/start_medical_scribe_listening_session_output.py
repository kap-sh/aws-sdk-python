"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartMedicalScribeListeningSessionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.medical_scribe_language_code
    import aws_sdk_connecthealth.types.medical_scribe_media_encoding
    import aws_sdk_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import aws_sdk_connecthealth.types.medical_scribe_output_stream
    import aws_sdk_connecthealth.types.request_id
    import aws_sdk_connecthealth.types.scribe_session_id
    import aws_sdk_connecthealth.types.subscription_id


class StartMedicalScribeListeningSessionOutput(TypedDict):
    session_id: NotRequired[
        "aws_sdk_connecthealth.types.scribe_session_id.ScribeSessionId"
    ]
    """<p>The Session identifier</p>"""
    domain_id: NotRequired["aws_sdk_connecthealth.types.domain_id.DomainId"]
    """<p>The Domain identifier</p>"""
    subscription_id: NotRequired[
        "aws_sdk_connecthealth.types.subscription_id.SubscriptionId"
    ]
    """<p>The Subscription identifier</p>"""
    request_id: NotRequired["aws_sdk_connecthealth.types.request_id.RequestId"]
    """<p>The Request identifier</p>"""
    language_code: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The Language Code for the audio in the session</p>"""
    media_sample_rate_hertz: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    ]
    """<p>The sample rate of the input audio</p>"""
    media_encoding: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    ]
    """<p>The encoding for the input audio</p>"""
    response_stream: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_output_stream.MedicalScribeOutputStream"
    ]
    """<p>The output stream containing transcript events</p>"""
