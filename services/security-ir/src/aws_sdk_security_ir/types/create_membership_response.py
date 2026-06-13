"""Generated from Smithy shape ``com.amazonaws.securityir#CreateMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.membership_id


class CreateMembershipResponse(TypedDict):
    membership_id: "aws_sdk_security_ir.types.membership_id.MembershipId"
    """<p>Response element for CreateMembership providing the newly created membership ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipResponse) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    return out


def deserialize_json(data: dict) -> CreateMembershipResponse:
    out: CreateMembershipResponse = {}  # type: ignore[typeddict-item]
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("CreateMembershipResponse.membership_id required")
    return out
