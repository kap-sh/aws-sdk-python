"""Generated from Smithy shape ``com.amazonaws.securityir#CancelMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.membership_id


class CancelMembershipRequest(TypedDict, closed=True):
    membership_id: "capo_security_ir.types.membership_id.MembershipId"
    """<p>Required element used in combination with CancelMembershipRequest to identify the membership ID to cancel. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelMembershipRequest:
    out: CancelMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
