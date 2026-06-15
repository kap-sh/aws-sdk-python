"""Generated from Smithy shape ``com.amazonaws.kendra#GroupMembers``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.member_groups
    import aws_sdk_kendra.types.member_users
    import aws_sdk_kendra.types.s3_path


class GroupMembers(TypedDict):
    member_groups: NotRequired["aws_sdk_kendra.types.member_groups.MemberGroups"]
    r"""<p>A list of users that belong to a group. This can also include sub groups. For example, the sub groups \"Research\", \"Engineering\", and \"Sales and Marketing\" all belong to the group \"Company A\".</p>"""
    member_users: NotRequired["aws_sdk_kendra.types.member_users.MemberUsers"]
    r"""<p>A list of users that belong to a group. For example, a list of interns all belong to the \"Interns\" group.</p>"""
    s3_pathfor_group_members: NotRequired["aws_sdk_kendra.types.s3_path.S3Path"]
    r"""<p>If you have more than 1000 users and/or sub groups for a single group, you need to provide the path to the S3 file that lists your users and sub groups for a group. Your sub groups can contain more than 1000 users, but the list of sub groups that belong to a group (and/or users) must be no more than 1000.</p> <p>You can download this <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/samples/group_members.zip\">example S3 file</a> that uses the correct format for listing group members. Note, <code>dataSourceId</code> is optional. The value of <code>type</code> for a group is always <code>GROUP</code> and for a user it is always <code>USER</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupMembers) -> dict:
    out: dict = {}
    if "member_groups" in value:
        import aws_sdk_kendra.types.member_groups

        out["MemberGroups"] = aws_sdk_kendra.types.member_groups.serialize_aws_json_1_1(
            value["member_groups"]
        )
    if "member_users" in value:
        import aws_sdk_kendra.types.member_users

        out["MemberUsers"] = aws_sdk_kendra.types.member_users.serialize_aws_json_1_1(
            value["member_users"]
        )
    if "s3_pathfor_group_members" in value:
        import aws_sdk_kendra.types.s3_path

        out["S3PathforGroupMembers"] = (
            aws_sdk_kendra.types.s3_path.serialize_aws_json_1_1(
                value["s3_pathfor_group_members"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupMembers:
    out: GroupMembers = {}  # type: ignore[typeddict-item]
    if "MemberGroups" in data:
        import aws_sdk_kendra.types.member_groups

        out["member_groups"] = (
            aws_sdk_kendra.types.member_groups.deserialize_aws_json_1_1(
                data["MemberGroups"]
            )
        )
    if "MemberUsers" in data:
        import aws_sdk_kendra.types.member_users

        out["member_users"] = (
            aws_sdk_kendra.types.member_users.deserialize_aws_json_1_1(
                data["MemberUsers"]
            )
        )
    if "S3PathforGroupMembers" in data:
        import aws_sdk_kendra.types.s3_path

        out["s3_pathfor_group_members"] = (
            aws_sdk_kendra.types.s3_path.deserialize_aws_json_1_1(
                data["S3PathforGroupMembers"]
            )
        )
    return out
