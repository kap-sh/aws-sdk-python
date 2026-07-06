"""Generated from Smithy shape ``com.amazonaws.eks#AccessEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list
    import aws_sdk_eks.types.tag_map
    import aws_sdk_eks.types.timestamp


class AccessEntry(TypedDict, closed=True):
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of your cluster.</p>"""
    principal_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of the IAM principal for the access entry. If you ever delete the IAM principal with this ARN, the access entry isn't automatically deleted. We recommend that you delete the access entry with an ARN for an IAM principal that you delete. If you don't delete the access entry and ever recreate the IAM principal, even if it has the same ARN, the access entry won't work. This is because even though the ARN is the same for the recreated IAM principal, the <code>roleID</code> or <code>userID</code> (you can see this with the Security Token Service <code>GetCallerIdentity</code> API) is different for the recreated IAM principal than it was for the original IAM principal. Even though you don't see the IAM principal's <code>roleID</code> or <code>userID</code> for an access entry, Amazon EKS stores it with the access entry.</p>"""
    kubernetes_groups: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>A <code>name</code> that you've specified in a Kubernetes <code>RoleBinding</code> or <code>ClusterRoleBinding</code> object so that Kubernetes authorizes the <code>principalARN</code> access to cluster objects.</p>"""
    access_entry_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of the access entry.</p>"""
    created_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp at object creation.</p>"""
    modified_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp for the last modification to the object.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    username: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>name</code> of a user that can authenticate to your cluster.</p>"""
    type: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The type of the access entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessEntry) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    if "kubernetes_groups" in value:
        import aws_sdk_eks.types.string_list

        out["kubernetesGroups"] = aws_sdk_eks.types.string_list.serialize_json(
            value["kubernetes_groups"]
        )
    if "access_entry_arn" in value:
        out["accessEntryArn"] = value["access_entry_arn"]
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
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    if "username" in value:
        out["username"] = value["username"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AccessEntry:
    out: AccessEntry = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    if "kubernetesGroups" in data:
        import aws_sdk_eks.types.string_list

        out["kubernetes_groups"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["kubernetesGroups"]
        )
    if "accessEntryArn" in data:
        out["access_entry_arn"] = data["accessEntryArn"]
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
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    if "username" in data:
        out["username"] = data["username"]
    if "type" in data:
        out["type"] = data["type"]
    return out
