"""Generated from Smithy shape ``com.amazonaws.identitystore#CreateGroupMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.resource_id


class CreateGroupMembershipResponse(TypedDict):
    membership_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a newly created <code>GroupMembership</code> in an identity store.</p>"""
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGroupMembershipResponse) -> dict:
    out: dict = {}
    out["MembershipId"] = value["membership_id"]
    out["IdentityStoreId"] = value["identity_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGroupMembershipResponse:
    out: CreateGroupMembershipResponse = {}  # type: ignore[typeddict-item]
    if "MembershipId" in data:
        out["membership_id"] = data["MembershipId"]
    else:
        raise DeserializationError(
            "CreateGroupMembershipResponse.membership_id required"
        )
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "CreateGroupMembershipResponse.identity_store_id required"
        )
    return out
