"""Generated from Smithy shape ``com.amazonaws.identitystore#GetGroupMembershipIdRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.member_id
    import aws_sdk_identitystore.types.resource_id


class GetGroupMembershipIdRequest(TypedDict):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    group_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p>"""
    member_id: "aws_sdk_identitystore.types.member_id.MemberId"
    """<p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGroupMembershipIdRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["GroupId"] = value["group_id"]
    import aws_sdk_identitystore.types.member_id

    out["MemberId"] = aws_sdk_identitystore.types.member_id.serialize_aws_json_1_1(
        value["member_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGroupMembershipIdRequest:
    out: GetGroupMembershipIdRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "GetGroupMembershipIdRequest.identity_store_id required"
        )
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("GetGroupMembershipIdRequest.group_id required")
    if "MemberId" in data:
        import aws_sdk_identitystore.types.member_id

        out["member_id"] = (
            aws_sdk_identitystore.types.member_id.deserialize_aws_json_1_1(
                data["MemberId"]
            )
        )
    else:
        raise DeserializationError("GetGroupMembershipIdRequest.member_id required")
    return out
