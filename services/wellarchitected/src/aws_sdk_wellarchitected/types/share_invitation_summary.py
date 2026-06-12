"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareInvitationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.aws_account_id
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.lens_name
    import aws_sdk_wellarchitected.types.permission_type
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.profile_name
    import aws_sdk_wellarchitected.types.share_invitation_id
    import aws_sdk_wellarchitected.types.share_resource_type
    import aws_sdk_wellarchitected.types.shared_with
    import aws_sdk_wellarchitected.types.template_arn
    import aws_sdk_wellarchitected.types.template_name
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_name


class ShareInvitationSummary(TypedDict):
    share_invitation_id: NotRequired[
        "aws_sdk_wellarchitected.types.share_invitation_id.ShareInvitationId"
    ]
    """<p>The ID assigned to the share invitation.</p>"""
    shared_by: NotRequired["aws_sdk_wellarchitected.types.aws_account_id.AwsAccountId"]
    shared_with: NotRequired["aws_sdk_wellarchitected.types.shared_with.SharedWith"]
    permission_type: NotRequired[
        "aws_sdk_wellarchitected.types.permission_type.PermissionType"
    ]
    share_resource_type: NotRequired[
        "aws_sdk_wellarchitected.types.share_resource_type.ShareResourceType"
    ]
    """<p>The resource type of the share invitation.</p>"""
    workload_name: NotRequired[
        "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
    ]
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    lens_name: NotRequired["aws_sdk_wellarchitected.types.lens_name.LensName"]
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The ARN for the lens.</p>"""
    profile_name: NotRequired["aws_sdk_wellarchitected.types.profile_name.ProfileName"]
    """<p>The profile name.</p>"""
    profile_arn: NotRequired["aws_sdk_wellarchitected.types.profile_arn.ProfileArn"]
    """<p>The profile ARN.</p>"""
    template_name: NotRequired[
        "aws_sdk_wellarchitected.types.template_name.TemplateName"
    ]
    """<p>The name of the review template.</p>"""
    template_arn: NotRequired["aws_sdk_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShareInvitationSummary) -> dict:
    out: dict = {}
    if "share_invitation_id" in value:
        out["ShareInvitationId"] = value["share_invitation_id"]
    if "shared_by" in value:
        out["SharedBy"] = value["shared_by"]
    if "shared_with" in value:
        out["SharedWith"] = value["shared_with"]
    if "permission_type" in value:
        import aws_sdk_wellarchitected.types.permission_type

        out["PermissionType"] = (
            aws_sdk_wellarchitected.types.permission_type.serialize_json(
                value["permission_type"]
            )
        )
    if "share_resource_type" in value:
        import aws_sdk_wellarchitected.types.share_resource_type

        out["ShareResourceType"] = (
            aws_sdk_wellarchitected.types.share_resource_type.serialize_json(
                value["share_resource_type"]
            )
        )
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "lens_name" in value:
        out["LensName"] = value["lens_name"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "profile_arn" in value:
        out["ProfileArn"] = value["profile_arn"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    return out


def deserialize_json(data: dict) -> ShareInvitationSummary:
    out: ShareInvitationSummary = {}  # type: ignore[typeddict-item]
    if "ShareInvitationId" in data:
        out["share_invitation_id"] = data["ShareInvitationId"]
    if "SharedBy" in data:
        out["shared_by"] = data["SharedBy"]
    if "SharedWith" in data:
        out["shared_with"] = data["SharedWith"]
    if "PermissionType" in data:
        import aws_sdk_wellarchitected.types.permission_type

        out["permission_type"] = (
            aws_sdk_wellarchitected.types.permission_type.deserialize_json(
                data["PermissionType"]
            )
        )
    if "ShareResourceType" in data:
        import aws_sdk_wellarchitected.types.share_resource_type

        out["share_resource_type"] = (
            aws_sdk_wellarchitected.types.share_resource_type.deserialize_json(
                data["ShareResourceType"]
            )
        )
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "LensName" in data:
        out["lens_name"] = data["LensName"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "ProfileName" in data:
        out["profile_name"] = data["ProfileName"]
    if "ProfileArn" in data:
        out["profile_arn"] = data["ProfileArn"]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    return out
