"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendOTPMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.send_otp_message_request_parameters


class SendOTPMessageRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique ID of your Amazon Pinpoint application.</p>"""
    send_otp_message_request_parameters: NotRequired[
        "aws_sdk_pinpoint.types.send_otp_message_request_parameters.SendOTPMessageRequestParameters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SendOTPMessageRequest) -> dict:
    out: dict = {}
    if "send_otp_message_request_parameters" in value:
        import aws_sdk_pinpoint.types.send_otp_message_request_parameters

        out["SendOTPMessageRequestParameters"] = (
            aws_sdk_pinpoint.types.send_otp_message_request_parameters.serialize_json(
                value["send_otp_message_request_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendOTPMessageRequest:
    out: SendOTPMessageRequest = {}  # type: ignore[typeddict-item]
    if "SendOTPMessageRequestParameters" in data:
        import aws_sdk_pinpoint.types.send_otp_message_request_parameters

        out["send_otp_message_request_parameters"] = (
            aws_sdk_pinpoint.types.send_otp_message_request_parameters.deserialize_json(
                data["SendOTPMessageRequestParameters"]
            )
        )
    return out
