"""Generated from Smithy shape ``com.amazonaws.pinpoint#VerifyOTPMessageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.verification_response


class VerifyOTPMessageResponse(TypedDict):
    verification_response: NotRequired[
        "aws_sdk_pinpoint.types.verification_response.VerificationResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VerifyOTPMessageResponse) -> dict:
    out: dict = {}
    if "verification_response" in value:
        import aws_sdk_pinpoint.types.verification_response

        out["VerificationResponse"] = (
            aws_sdk_pinpoint.types.verification_response.serialize_json(
                value["verification_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerifyOTPMessageResponse:
    out: VerifyOTPMessageResponse = {}  # type: ignore[typeddict-item]
    if "VerificationResponse" in data:
        import aws_sdk_pinpoint.types.verification_response

        out["verification_response"] = (
            aws_sdk_pinpoint.types.verification_response.deserialize_json(
                data["VerificationResponse"]
            )
        )
    return out
