"""Generated from Smithy shape ``com.amazonaws.pinpoint#VerifyOTPMessageRequestParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class VerifyOTPMessageRequestParameters(TypedDict, closed=True):
    destination_identity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The destination identity to send OTP to.</p>"""
    otp: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The OTP the end user provided for verification.</p>"""
    reference_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The reference identifier provided when the OTP was previously sent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyOTPMessageRequestParameters) -> dict:
    out: dict = {}
    if "destination_identity" in value:
        out["DestinationIdentity"] = value["destination_identity"]
    if "otp" in value:
        out["Otp"] = value["otp"]
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    return out


def deserialize_json(data: dict) -> VerifyOTPMessageRequestParameters:
    out: VerifyOTPMessageRequestParameters = {}  # type: ignore[typeddict-item]
    if "DestinationIdentity" in data:
        out["destination_identity"] = data["DestinationIdentity"]
    if "Otp" in data:
        out["otp"] = data["Otp"]
    if "ReferenceId" in data:
        out["reference_id"] = data["ReferenceId"]
    return out
