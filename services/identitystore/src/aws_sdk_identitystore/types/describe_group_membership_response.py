"""Generated from Smithy shape ``com.amazonaws.identitystore#DescribeGroupMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.date_type
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.member_id
    import aws_sdk_identitystore.types.resource_id
    import aws_sdk_identitystore.types.string_type


class DescribeGroupMembershipResponse(TypedDict):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    membership_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a <code>GroupMembership</code> in an identity store.</p>"""
    group_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p>"""
    member_id: "aws_sdk_identitystore.types.member_id.MemberId"
    created_at: NotRequired["aws_sdk_identitystore.types.date_type.DateType"]
    """<p>The date and time the group membership was created.</p>"""
    updated_at: NotRequired["aws_sdk_identitystore.types.date_type.DateType"]
    """<p>The date and time the group membership was last updated.</p>"""
    created_by: NotRequired["aws_sdk_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that created the group membership.</p>"""
    updated_by: NotRequired["aws_sdk_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that last updated the group membership.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGroupMembershipResponse) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["MembershipId"] = value["membership_id"]
    out["GroupId"] = value["group_id"]
    import aws_sdk_identitystore.types.member_id

    out["MemberId"] = aws_sdk_identitystore.types.member_id.serialize_aws_json_1_1(
        value["member_id"]
    )
    if "created_at" in value:
        import aws_sdk_identitystore.types.date_type

        out["CreatedAt"] = aws_sdk_identitystore.types.date_type.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_identitystore.types.date_type

        out["UpdatedAt"] = aws_sdk_identitystore.types.date_type.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGroupMembershipResponse:
    out: DescribeGroupMembershipResponse = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "DescribeGroupMembershipResponse.identity_store_id required"
        )
    if "MembershipId" in data:
        out["membership_id"] = data["MembershipId"]
    else:
        raise DeserializationError(
            "DescribeGroupMembershipResponse.membership_id required"
        )
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("DescribeGroupMembershipResponse.group_id required")
    if "MemberId" in data:
        import aws_sdk_identitystore.types.member_id

        out["member_id"] = (
            aws_sdk_identitystore.types.member_id.deserialize_aws_json_1_1(
                data["MemberId"]
            )
        )
    else:
        raise DeserializationError("DescribeGroupMembershipResponse.member_id required")
    if "CreatedAt" in data:
        import aws_sdk_identitystore.types.date_type

        out["created_at"] = (
            aws_sdk_identitystore.types.date_type.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_identitystore.types.date_type

        out["updated_at"] = (
            aws_sdk_identitystore.types.date_type.deserialize_aws_json_1_1(
                data["UpdatedAt"]
            )
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "UpdatedBy" in data:
        out["updated_by"] = data["UpdatedBy"]
    return out
