"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.aws_account_id
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.profile_description
    import aws_sdk_wellarchitected.types.profile_name
    import aws_sdk_wellarchitected.types.profile_version
    import aws_sdk_wellarchitected.types.timestamp


class ProfileSummary(TypedDict, closed=True):
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
    owner: NotRequired["aws_sdk_wellarchitected.types.aws_account_id.AwsAccountId"]
    created_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileSummary) -> dict:
    out: dict = {}
    if "profile_arn" in value:
        out["ProfileArn"] = value["profile_arn"]
    if "profile_version" in value:
        out["ProfileVersion"] = value["profile_version"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "profile_description" in value:
        out["ProfileDescription"] = value["profile_description"]
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
    return out


def deserialize_json(data: dict) -> ProfileSummary:
    out: ProfileSummary = {}  # type: ignore[typeddict-item]
    if "ProfileArn" in data:
        out["profile_arn"] = data["ProfileArn"]
    if "ProfileVersion" in data:
        out["profile_version"] = data["ProfileVersion"]
    if "ProfileName" in data:
        out["profile_name"] = data["ProfileName"]
    if "ProfileDescription" in data:
        out["profile_description"] = data["ProfileDescription"]
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
    return out
