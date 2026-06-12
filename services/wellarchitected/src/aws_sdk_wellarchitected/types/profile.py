"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Profile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.aws_account_id
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.profile_description
    import aws_sdk_wellarchitected.types.profile_name
    import aws_sdk_wellarchitected.types.profile_questions
    import aws_sdk_wellarchitected.types.profile_version
    import aws_sdk_wellarchitected.types.share_invitation_id
    import aws_sdk_wellarchitected.types.tag_map
    import aws_sdk_wellarchitected.types.timestamp


class Profile(TypedDict):
    profile_arn: NotRequired["aws_sdk_wellarchitected.types.profile_arn.ProfileArn"]
    """<p>The profile ARN.</p>"""
    profile_version: NotRequired[
        "aws_sdk_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>The profile version.</p>"""
    profile_name: NotRequired["aws_sdk_wellarchitected.types.profile_name.ProfileName"]
    """<p>The profile name.</p>"""
    profile_description: NotRequired[
        "aws_sdk_wellarchitected.types.profile_description.ProfileDescription"
    ]
    """<p>The profile description.</p>"""
    profile_questions: NotRequired[
        "aws_sdk_wellarchitected.types.profile_questions.ProfileQuestions"
    ]
    """<p>Profile questions.</p>"""
    owner: NotRequired["aws_sdk_wellarchitected.types.aws_account_id.AwsAccountId"]
    created_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    share_invitation_id: NotRequired[
        "aws_sdk_wellarchitected.types.share_invitation_id.ShareInvitationId"
    ]
    """<p>The ID assigned to the share invitation.</p>"""
    tags: NotRequired["aws_sdk_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags assigned to the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Profile) -> dict:
    out: dict = {}
    if "profile_arn" in value:
        out["ProfileArn"] = value["profile_arn"]
    if "profile_version" in value:
        out["ProfileVersion"] = value["profile_version"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "profile_description" in value:
        out["ProfileDescription"] = value["profile_description"]
    if "profile_questions" in value:
        import aws_sdk_wellarchitected.types.profile_questions

        out["ProfileQuestions"] = (
            aws_sdk_wellarchitected.types.profile_questions.serialize_json(
                value["profile_questions"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "created_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["CreatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["UpdatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "share_invitation_id" in value:
        out["ShareInvitationId"] = value["share_invitation_id"]
    if "tags" in value:
        import aws_sdk_wellarchitected.types.tag_map

        out["Tags"] = aws_sdk_wellarchitected.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> Profile:
    out: Profile = {}  # type: ignore[typeddict-item]
    if "ProfileArn" in data:
        out["profile_arn"] = data["ProfileArn"]
    if "ProfileVersion" in data:
        out["profile_version"] = data["ProfileVersion"]
    if "ProfileName" in data:
        out["profile_name"] = data["ProfileName"]
    if "ProfileDescription" in data:
        out["profile_description"] = data["ProfileDescription"]
    if "ProfileQuestions" in data:
        import aws_sdk_wellarchitected.types.profile_questions

        out["profile_questions"] = (
            aws_sdk_wellarchitected.types.profile_questions.deserialize_json(
                data["ProfileQuestions"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "CreatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["created_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["updated_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "ShareInvitationId" in data:
        out["share_invitation_id"] = data["ShareInvitationId"]
    if "Tags" in data:
        import aws_sdk_wellarchitected.types.tag_map

        out["tags"] = aws_sdk_wellarchitected.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
