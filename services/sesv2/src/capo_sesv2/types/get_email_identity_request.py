"""Generated from Smithy shape ``com.amazonaws.sesv2#GetEmailIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.identity


class GetEmailIdentityRequest(TypedDict, closed=True):
    email_identity: "capo_sesv2.types.identity.Identity"
    """<p>The email identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailIdentityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEmailIdentityRequest:
    out: GetEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    return out
