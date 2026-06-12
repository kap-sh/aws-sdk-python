"""Generated from Smithy shape ``com.amazonaws.identitystore#DescribeGroupMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.resource_id


class DescribeGroupMembershipRequest(TypedDict):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    membership_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a <code>GroupMembership</code> in an identity store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGroupMembershipRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["MembershipId"] = value["membership_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGroupMembershipRequest:
    out: DescribeGroupMembershipRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "DescribeGroupMembershipRequest.identity_store_id required"
        )
    if "MembershipId" in data:
        out["membership_id"] = data["MembershipId"]
    else:
        raise DeserializationError(
            "DescribeGroupMembershipRequest.membership_id required"
        )
    return out
