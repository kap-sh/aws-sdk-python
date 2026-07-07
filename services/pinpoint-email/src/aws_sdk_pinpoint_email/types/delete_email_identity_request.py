"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeleteEmailIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.identity


class DeleteEmailIdentityRequest(TypedDict, closed=True):
    email_identity: "aws_sdk_pinpoint_email.types.identity.Identity"
    """<p>The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailIdentityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEmailIdentityRequest:
    out: DeleteEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
