"""Generated from Smithy shape ``com.amazonaws.pinpoint#VerifyOTPMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.verify_otp_message_request_parameters


class VerifyOTPMessageRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique ID of your Amazon Pinpoint application.</p>"""
    verify_otp_message_request_parameters: NotRequired[
        "capo_pinpoint.types.verify_otp_message_request_parameters.VerifyOTPMessageRequestParameters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VerifyOTPMessageRequest) -> dict:
    out: dict = {}
    if "verify_otp_message_request_parameters" in value:
        import capo_pinpoint.types.verify_otp_message_request_parameters

        out["VerifyOTPMessageRequestParameters"] = (
            capo_pinpoint.types.verify_otp_message_request_parameters.serialize_json(
                value["verify_otp_message_request_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerifyOTPMessageRequest:
    out: VerifyOTPMessageRequest = {}  # type: ignore[typeddict-item]
    if "VerifyOTPMessageRequestParameters" in data:
        import capo_pinpoint.types.verify_otp_message_request_parameters

        out["verify_otp_message_request_parameters"] = (
            capo_pinpoint.types.verify_otp_message_request_parameters.deserialize_json(
                data["VerifyOTPMessageRequestParameters"]
            )
        )
    return out
