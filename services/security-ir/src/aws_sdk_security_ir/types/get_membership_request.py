"""Generated from Smithy shape ``com.amazonaws.securityir#GetMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.membership_id


class GetMembershipRequest(TypedDict):
    membership_id: "aws_sdk_security_ir.types.membership_id.MembershipId"
    """<p>Required element for GetMembership to identify the membership ID to query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMembershipRequest:
    out: GetMembershipRequest = {}  # type: ignore[typeddict-item]
    return out
