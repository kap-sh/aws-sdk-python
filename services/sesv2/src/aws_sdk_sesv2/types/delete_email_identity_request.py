"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteEmailIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.identity


class DeleteEmailIdentityRequest(TypedDict, closed=True):
    email_identity: "aws_sdk_sesv2.types.identity.Identity"
    """<p>The identity (that is, the email address or domain) to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailIdentityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEmailIdentityRequest:
    out: DeleteEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
