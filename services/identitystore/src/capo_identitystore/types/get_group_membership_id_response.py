"""Generated from Smithy shape ``com.amazonaws.identitystore#GetGroupMembershipIdResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_id


class GetGroupMembershipIdResponse(TypedDict, closed=True):
    membership_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a <code>GroupMembership</code> in an identity store.</p>"""
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGroupMembershipIdResponse) -> dict:
    out: dict = {}
    out["MembershipId"] = value["membership_id"]
    out["IdentityStoreId"] = value["identity_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGroupMembershipIdResponse:
    out: GetGroupMembershipIdResponse = {}  # type: ignore[typeddict-item]
    if "MembershipId" in data:
        out["membership_id"] = data["MembershipId"]
    else:
        raise DeserializationError(
            "GetGroupMembershipIdResponse.membership_id required"
        )
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "GetGroupMembershipIdResponse.identity_store_id required"
        )
    return out
