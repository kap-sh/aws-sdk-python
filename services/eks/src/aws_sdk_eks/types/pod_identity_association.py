"""Generated from Smithy shape ``com.amazonaws.eks#PodIdentityAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.tag_map
    import aws_sdk_eks.types.timestamp


class PodIdentityAssociation(TypedDict):
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the cluster that the association is in.</p>"""
    namespace: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the Kubernetes namespace inside the cluster to create the association in. The service account and the Pods that use the service account must be in this namespace.</p>"""
    service_account: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.</p>"""
    role_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with the service account. The EKS Pod Identity agent manages credentials to assume this role for applications in the containers in the Pods that use this service account.</p>"""
    association_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    association_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ID of the association.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource – 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length – 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length – 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    created_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The timestamp that the association was created at.</p>"""
    modified_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The most recent timestamp that the association was modified at.</p>"""
    owner_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>If defined, the EKS Pod Identity association is owned by an Amazon EKS add-on.</p>"""
    disable_session_tags: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>The state of the automatic sessions tags. The value of <i>true</i> disables these tags.</p> <p>EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to Amazon Web Services resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags\">List of session tags added by EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    target_role_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.</p>"""
    external_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The unique identifier for this EKS Pod Identity association for a target IAM role. You put this value in the trust policy of the target role, in a <code>Condition</code> to match the <code>sts.ExternalId</code>. This ensures that the target role can only be assumed by this association. This prevents the <i>confused deputy problem</i>. For more information about the confused deputy problem, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html\">The confused deputy problem</a> in the <i>IAM User Guide</i>.</p> <p>If you want to use the same target role with multiple associations or other roles, use independent statements in the trust policy to allow <code>sts:AssumeRole</code> access from each role.</p>"""
    policy: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PodIdentityAssociation) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "service_account" in value:
        out["serviceAccount"] = value["service_account"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "association_arn" in value:
        out["associationArn"] = value["association_arn"]
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    if "created_at" in value:
        import aws_sdk_eks.types.timestamp

        out["createdAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "modified_at" in value:
        import aws_sdk_eks.types.timestamp

        out["modifiedAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["modified_at"]
        )
    if "owner_arn" in value:
        out["ownerArn"] = value["owner_arn"]
    if "disable_session_tags" in value:
        out["disableSessionTags"] = value["disable_session_tags"]
    if "target_role_arn" in value:
        out["targetRoleArn"] = value["target_role_arn"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PodIdentityAssociation:
    out: PodIdentityAssociation = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "serviceAccount" in data:
        out["service_account"] = data["serviceAccount"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "associationArn" in data:
        out["association_arn"] = data["associationArn"]
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    if "createdAt" in data:
        import aws_sdk_eks.types.timestamp

        out["created_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "modifiedAt" in data:
        import aws_sdk_eks.types.timestamp

        out["modified_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    if "ownerArn" in data:
        out["owner_arn"] = data["ownerArn"]
    if "disableSessionTags" in data:
        out["disable_session_tags"] = data["disableSessionTags"]
    if "targetRoleArn" in data:
        out["target_role_arn"] = data["targetRoleArn"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
