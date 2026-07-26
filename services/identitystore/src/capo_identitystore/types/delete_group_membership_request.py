"""Generated from Smithy shape ``com.amazonaws.identitystore#DeleteGroupMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_id


class DeleteGroupMembershipRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    membership_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a <code>GroupMembership</code> in an identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGroupMembershipRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["MembershipId"] = value["membership_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGroupMembershipRequest:
    out: DeleteGroupMembershipRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "DeleteGroupMembershipRequest.identity_store_id required"
        )
    if "MembershipId" in data:
        out["membership_id"] = data["MembershipId"]
    else:
        raise DeserializationError(
            "DeleteGroupMembershipRequest.membership_id required"
        )
    return out
