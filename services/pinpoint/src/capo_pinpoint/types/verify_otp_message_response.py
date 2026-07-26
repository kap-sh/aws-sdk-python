"""Generated from Smithy shape ``com.amazonaws.pinpoint#VerifyOTPMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.verification_response


class VerifyOTPMessageResponse(TypedDict, closed=True):
    verification_response: NotRequired[
        "capo_pinpoint.types.verification_response.VerificationResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VerifyOTPMessageResponse) -> dict:
    out: dict = {}
    if "verification_response" in value:
        import capo_pinpoint.types.verification_response

        out["VerificationResponse"] = (
            capo_pinpoint.types.verification_response.serialize_json(
                value["verification_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerifyOTPMessageResponse:
    out: VerifyOTPMessageResponse = {}  # type: ignore[typeddict-item]
    if "VerificationResponse" in data:
        import capo_pinpoint.types.verification_response

        out["verification_response"] = (
            capo_pinpoint.types.verification_response.deserialize_json(
                data["VerificationResponse"]
            )
        )
    return out
