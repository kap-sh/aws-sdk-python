"""Generated from Smithy shape ``com.amazonaws.qbusiness#GroupMembers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.member_groups
    import aws_sdk_qbusiness.types.member_users
    import aws_sdk_qbusiness.types.s3


class GroupMembers(TypedDict, closed=True):
    member_groups: NotRequired["aws_sdk_qbusiness.types.member_groups.MemberGroups"]
    r"""<p>A list of sub groups that belong to a group. For example, the sub groups \"Research\", \"Engineering\", and \"Sales and Marketing\" all belong to the group \"Company\".</p>"""
    member_users: NotRequired["aws_sdk_qbusiness.types.member_users.MemberUsers"]
    r"""<p>A list of users that belong to a group. For example, a list of interns all belong to the \"Interns\" group.</p>"""
    s3_path_for_group_members: NotRequired["aws_sdk_qbusiness.types.s3.S3"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupMembers) -> dict:
    out: dict = {}
    if "member_groups" in value:
        import aws_sdk_qbusiness.types.member_groups

        out["memberGroups"] = aws_sdk_qbusiness.types.member_groups.serialize_json(
            value["member_groups"]
        )
    if "member_users" in value:
        import aws_sdk_qbusiness.types.member_users

        out["memberUsers"] = aws_sdk_qbusiness.types.member_users.serialize_json(
            value["member_users"]
        )
    if "s3_path_for_group_members" in value:
        import aws_sdk_qbusiness.types.s3

        out["s3PathForGroupMembers"] = aws_sdk_qbusiness.types.s3.serialize_json(
            value["s3_path_for_group_members"]
        )
    return out


def deserialize_json(data: dict) -> GroupMembers:
    out: GroupMembers = {}  # type: ignore[typeddict-item]
    if "memberGroups" in data:
        import aws_sdk_qbusiness.types.member_groups

        out["member_groups"] = aws_sdk_qbusiness.types.member_groups.deserialize_json(
            data["memberGroups"]
        )
    if "memberUsers" in data:
        import aws_sdk_qbusiness.types.member_users

        out["member_users"] = aws_sdk_qbusiness.types.member_users.deserialize_json(
            data["memberUsers"]
        )
    if "s3PathForGroupMembers" in data:
        import aws_sdk_qbusiness.types.s3

        out["s3_path_for_group_members"] = aws_sdk_qbusiness.types.s3.deserialize_json(
            data["s3PathForGroupMembers"]
        )
    return out
