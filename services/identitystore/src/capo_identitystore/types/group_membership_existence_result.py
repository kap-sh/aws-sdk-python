"""Generated from Smithy shape ``com.amazonaws.identitystore#GroupMembershipExistenceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_identitystore.types.boolean_type
    import capo_identitystore.types.member_id
    import capo_identitystore.types.resource_id


class GroupMembershipExistenceResult(TypedDict, closed=True):
    group_id: NotRequired["capo_identitystore.types.resource_id.ResourceId"]
    """<p>The identifier for a group in the identity store.</p>"""
    member_id: NotRequired["capo_identitystore.types.member_id.MemberId"]
    """<p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>"""
    membership_exists: "capo_identitystore.types.boolean_type.BooleanType"
    """<p>Indicates whether a membership relation exists or not.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupMembershipExistenceResult) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "member_id" in value:
        import capo_identitystore.types.member_id

        out["MemberId"] = capo_identitystore.types.member_id.serialize_aws_json_1_1(
            value["member_id"]
        )
    out["MembershipExists"] = value.get("membership_exists", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupMembershipExistenceResult:
    out: GroupMembershipExistenceResult = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "MemberId" in data:
        import capo_identitystore.types.member_id

        out["member_id"] = capo_identitystore.types.member_id.deserialize_aws_json_1_1(
            data["MemberId"]
        )
    if "MembershipExists" in data:
        out["membership_exists"] = data["MembershipExists"]
    else:
        out["membership_exists"] = False
    return out
