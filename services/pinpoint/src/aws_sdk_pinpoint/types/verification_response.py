"""Generated from Smithy shape ``com.amazonaws.pinpoint#VerificationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean


class VerificationResponse(TypedDict):
    valid: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the OTP is valid or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerificationResponse) -> dict:
    out: dict = {}
    if "valid" in value:
        out["Valid"] = value["valid"]
    return out


def deserialize_json(data: dict) -> VerificationResponse:
    out: VerificationResponse = {}  # type: ignore[typeddict-item]
    if "Valid" in data:
        out["valid"] = data["Valid"]
    return out
