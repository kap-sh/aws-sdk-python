"""Generated from Smithy shape ``com.amazonaws.eks#UpdateNodegroupVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boolean
    import aws_sdk_eks.types.launch_template_specification
    import aws_sdk_eks.types.string


class UpdateNodegroupVersionRequest(TypedDict, closed=True):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    nodegroup_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the managed node group to update.</p>"""
    version: NotRequired["aws_sdk_eks.types.string.String"]
    r"""<p>The Kubernetes version to update to. If no version is specified, then the node group will be updated to match the cluster's current Kubernetes version, and the latest available AMI for that version will be used. You can also specify the Kubernetes version of the cluster to update the node group to the latest AMI version of the cluster's Kubernetes version. If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>version</code>, or the node group update will fail. For more information about using launch templates with Amazon EKS, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    release_version: NotRequired["aws_sdk_eks.types.string.String"]
    r"""<p>The AMI version of the Amazon EKS optimized AMI to use for the update. By default, the latest available AMI version for the node group's Kubernetes version is used. For information about Linux versions, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html\">Amazon EKS optimized Amazon Linux AMI versions</a> in the <i>Amazon EKS User Guide</i>. Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html\">Amazon EKS optimized Windows AMI versions</a> in the <i>Amazon EKS User Guide</i>.</p> <p>If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>releaseVersion</code>, or the node group update will fail. For more information about using launch templates with Amazon EKS, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html\">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    launch_template: NotRequired[
        "aws_sdk_eks.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>An object representing a node group's launch template specification. You can only update a node group using a launch template if the node group was originally deployed with a launch template. When updating, you must specify the same launch template ID or name that was used to create the node group.</p>"""
    force: "aws_sdk_eks.types.boolean.Boolean"
    """<p>Force the update if any <code>Pod</code> on the existing node group can't be drained due to a <code>Pod</code> disruption budget issue. If an update fails because all Pods can't be drained, you can force the update after it fails to terminate the old node whether or not any <code>Pod</code> is running on the node.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodegroupVersionRequest) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "release_version" in value:
        out["releaseVersion"] = value["release_version"]
    if "launch_template" in value:
        import aws_sdk_eks.types.launch_template_specification

        out["launchTemplate"] = (
            aws_sdk_eks.types.launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    out["force"] = value.get("force", False)
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpdateNodegroupVersionRequest:
    out: UpdateNodegroupVersionRequest = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    if "releaseVersion" in data:
        out["release_version"] = data["releaseVersion"]
    if "launchTemplate" in data:
        import aws_sdk_eks.types.launch_template_specification

        out["launch_template"] = (
            aws_sdk_eks.types.launch_template_specification.deserialize_json(
                data["launchTemplate"]
            )
        )
    if "force" in data:
        out["force"] = data["force"]
    else:
        out["force"] = False
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
