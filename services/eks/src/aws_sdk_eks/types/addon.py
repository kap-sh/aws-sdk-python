"""Generated from Smithy shape ``com.amazonaws.eks#Addon``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.addon_health
    import aws_sdk_eks.types.addon_namespace_config_response
    import aws_sdk_eks.types.addon_status
    import aws_sdk_eks.types.cluster_name
    import aws_sdk_eks.types.marketplace_information
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list
    import aws_sdk_eks.types.tag_map
    import aws_sdk_eks.types.timestamp


class Addon(TypedDict):
    addon_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the add-on.</p>"""
    cluster_name: NotRequired["aws_sdk_eks.types.cluster_name.ClusterName"]
    """<p>The name of your cluster.</p>"""
    status: NotRequired["aws_sdk_eks.types.addon_status.AddonStatus"]
    """<p>The status of the add-on.</p>"""
    addon_version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The version of the add-on.</p>"""
    health: NotRequired["aws_sdk_eks.types.addon_health.AddonHealth"]
    """<p>An object that represents the health of the add-on.</p>"""
    addon_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the add-on.</p>"""
    created_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp at object creation.</p>"""
    modified_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp for the last modification to the object.</p>"""
    service_account_role_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that's bound to the Kubernetes <code>ServiceAccount</code> object that the add-on uses.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    publisher: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The publisher of the add-on.</p>"""
    owner: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The owner of the add-on.</p>"""
    marketplace_information: NotRequired[
        "aws_sdk_eks.types.marketplace_information.MarketplaceInformation"
    ]
    """<p>Information about an Amazon EKS add-on from the Amazon Web Services Marketplace.</p>"""
    configuration_values: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The configuration values that you provided.</p>"""
    pod_identity_associations: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    r"""<p>An array of EKS Pod Identity associations owned by the add-on. Each association maps a role to a service account in a namespace in the cluster.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html\">Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    namespace_config: NotRequired[
        "aws_sdk_eks.types.addon_namespace_config_response.AddonNamespaceConfigResponse"
    ]
    """<p>The namespace configuration for the addon. This specifies the Kubernetes namespace where the addon is installed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Addon) -> dict:
    out: dict = {}
    if "addon_name" in value:
        out["addonName"] = value["addon_name"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "status" in value:
        import aws_sdk_eks.types.addon_status

        out["status"] = aws_sdk_eks.types.addon_status.serialize_json(value["status"])
    if "addon_version" in value:
        out["addonVersion"] = value["addon_version"]
    if "health" in value:
        import aws_sdk_eks.types.addon_health

        out["health"] = aws_sdk_eks.types.addon_health.serialize_json(value["health"])
    if "addon_arn" in value:
        out["addonArn"] = value["addon_arn"]
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
    if "service_account_role_arn" in value:
        out["serviceAccountRoleArn"] = value["service_account_role_arn"]
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    if "publisher" in value:
        out["publisher"] = value["publisher"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "marketplace_information" in value:
        import aws_sdk_eks.types.marketplace_information

        out["marketplaceInformation"] = (
            aws_sdk_eks.types.marketplace_information.serialize_json(
                value["marketplace_information"]
            )
        )
    if "configuration_values" in value:
        out["configurationValues"] = value["configuration_values"]
    if "pod_identity_associations" in value:
        import aws_sdk_eks.types.string_list

        out["podIdentityAssociations"] = aws_sdk_eks.types.string_list.serialize_json(
            value["pod_identity_associations"]
        )
    if "namespace_config" in value:
        import aws_sdk_eks.types.addon_namespace_config_response

        out["namespaceConfig"] = (
            aws_sdk_eks.types.addon_namespace_config_response.serialize_json(
                value["namespace_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Addon:
    out: Addon = {}  # type: ignore[typeddict-item]
    if "addonName" in data:
        out["addon_name"] = data["addonName"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "status" in data:
        import aws_sdk_eks.types.addon_status

        out["status"] = aws_sdk_eks.types.addon_status.deserialize_json(data["status"])
    if "addonVersion" in data:
        out["addon_version"] = data["addonVersion"]
    if "health" in data:
        import aws_sdk_eks.types.addon_health

        out["health"] = aws_sdk_eks.types.addon_health.deserialize_json(data["health"])
    if "addonArn" in data:
        out["addon_arn"] = data["addonArn"]
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
    if "serviceAccountRoleArn" in data:
        out["service_account_role_arn"] = data["serviceAccountRoleArn"]
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    if "publisher" in data:
        out["publisher"] = data["publisher"]
    if "owner" in data:
        out["owner"] = data["owner"]
    if "marketplaceInformation" in data:
        import aws_sdk_eks.types.marketplace_information

        out["marketplace_information"] = (
            aws_sdk_eks.types.marketplace_information.deserialize_json(
                data["marketplaceInformation"]
            )
        )
    if "configurationValues" in data:
        out["configuration_values"] = data["configurationValues"]
    if "podIdentityAssociations" in data:
        import aws_sdk_eks.types.string_list

        out["pod_identity_associations"] = (
            aws_sdk_eks.types.string_list.deserialize_json(
                data["podIdentityAssociations"]
            )
        )
    if "namespaceConfig" in data:
        import aws_sdk_eks.types.addon_namespace_config_response

        out["namespace_config"] = (
            aws_sdk_eks.types.addon_namespace_config_response.deserialize_json(
                data["namespaceConfig"]
            )
        )
    return out
