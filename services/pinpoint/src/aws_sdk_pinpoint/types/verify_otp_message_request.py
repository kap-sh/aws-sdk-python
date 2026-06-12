"""Generated from Smithy shape ``com.amazonaws.pinpoint#VerifyOTPMessageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.verify_otp_message_request_parameters


class VerifyOTPMessageRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique ID of your Amazon Pinpoint application.</p>"""
    verify_otp_message_request_parameters: NotRequired[
        "aws_sdk_pinpoint.types.verify_otp_message_request_parameters.VerifyOTPMessageRequestParameters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VerifyOTPMessageRequest) -> dict:
    out: dict = {}
    if "verify_otp_message_request_parameters" in value:
        import aws_sdk_pinpoint.types.verify_otp_message_request_parameters

        out["VerifyOTPMessageRequestParameters"] = (
            aws_sdk_pinpoint.types.verify_otp_message_request_parameters.serialize_json(
                value["verify_otp_message_request_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerifyOTPMessageRequest:
    out: VerifyOTPMessageRequest = {}  # type: ignore[typeddict-item]
    if "VerifyOTPMessageRequestParameters" in data:
        import aws_sdk_pinpoint.types.verify_otp_message_request_parameters

        out["verify_otp_message_request_parameters"] = (
            aws_sdk_pinpoint.types.verify_otp_message_request_parameters.deserialize_json(
                data["VerifyOTPMessageRequestParameters"]
            )
        )
    return out
