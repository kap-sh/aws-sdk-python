"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetEmailIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.identity


class GetEmailIdentityRequest(TypedDict):
    email_identity: "aws_sdk_pinpoint_email.types.identity.Identity"
    """<p>The email identity that you want to retrieve details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailIdentityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEmailIdentityRequest:
    out: GetEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
