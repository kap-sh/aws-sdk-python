"""Generated from Smithy shape ``com.amazonaws.securityir#CancelMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.membership_id


class CancelMembershipResponse(TypedDict):
    membership_id: "aws_sdk_security_ir.types.membership_id.MembershipId"
    """<p>The response element providing responses for requests to CancelMembershipRequest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMembershipResponse) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    return out


def deserialize_json(data: dict) -> CancelMembershipResponse:
    out: CancelMembershipResponse = {}  # type: ignore[typeddict-item]
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("CancelMembershipResponse.membership_id required")
    return out
