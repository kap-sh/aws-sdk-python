"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareInvitation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.share_invitation_id
    import aws_sdk_wellarchitected.types.share_resource_type
    import aws_sdk_wellarchitected.types.template_arn
    import aws_sdk_wellarchitected.types.workload_id


class ShareInvitation(TypedDict):
    share_invitation_id: NotRequired[
        "aws_sdk_wellarchitected.types.share_invitation_id.ShareInvitationId"
    ]
    """<p>The ID assigned to the share invitation.</p>"""
    share_resource_type: NotRequired[
        "aws_sdk_wellarchitected.types.share_resource_type.ShareResourceType"
    ]
    """<p>The resource type of the share invitation.</p>"""
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    profile_arn: NotRequired["aws_sdk_wellarchitected.types.profile_arn.ProfileArn"]
    """<p>The profile ARN.</p>"""
    template_arn: NotRequired["aws_sdk_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShareInvitation) -> dict:
    out: dict = {}
    if "share_invitation_id" in value:
        out["ShareInvitationId"] = value["share_invitation_id"]
    if "share_resource_type" in value:
        import aws_sdk_wellarchitected.types.share_resource_type

        out["ShareResourceType"] = (
            aws_sdk_wellarchitected.types.share_resource_type.serialize_json(
                value["share_resource_type"]
            )
        )
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "profile_arn" in value:
        out["ProfileArn"] = value["profile_arn"]
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    return out


def deserialize_json(data: dict) -> ShareInvitation:
    out: ShareInvitation = {}  # type: ignore[typeddict-item]
    if "ShareInvitationId" in data:
        out["share_invitation_id"] = data["ShareInvitationId"]
    if "ShareResourceType" in data:
        import aws_sdk_wellarchitected.types.share_resource_type

        out["share_resource_type"] = (
            aws_sdk_wellarchitected.types.share_resource_type.deserialize_json(
                data["ShareResourceType"]
            )
        )
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "ProfileArn" in data:
        out["profile_arn"] = data["ProfileArn"]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    return out
