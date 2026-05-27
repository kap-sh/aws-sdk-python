"""Generated from Smithy shape ``com.amazonaws.eks#Capability``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.capability_configuration_response
    import aws_sdk_eks.types.capability_delete_propagation_policy
    import aws_sdk_eks.types.capability_health
    import aws_sdk_eks.types.capability_status
    import aws_sdk_eks.types.capability_type
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.tag_map
    import aws_sdk_eks.types.timestamp


class Capability(TypedDict):
    capability_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The unique name of the capability within the cluster.</p>"""
    arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the capability.</p>"""
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the Amazon EKS cluster that contains this capability.</p>"""
    type: NotRequired["aws_sdk_eks.types.capability_type.CapabilityType"]
    """<p>The type of capability. Valid values are <code>ACK</code>, <code>ARGOCD</code>, or <code>KRO</code>.</p>"""
    role_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the capability uses to interact with Amazon Web Services services.</p>"""
    status: NotRequired["aws_sdk_eks.types.capability_status.CapabilityStatus"]
    """<p>The current status of the capability. Valid values include:</p> <ul> <li> <p> <code>CREATING</code> – The capability is being created.</p> </li> <li> <p> <code>ACTIVE</code> – The capability is running and available.</p> </li> <li> <p> <code>UPDATING</code> – The capability is being updated.</p> </li> <li> <p> <code>DELETING</code> – The capability is being deleted.</p> </li> <li> <p> <code>CREATE_FAILED</code> – The capability creation failed.</p> </li> <li> <p> <code>UPDATE_FAILED</code> – The capability update failed.</p> </li> <li> <p> <code>DELETE_FAILED</code> – The capability deletion failed.</p> </li> </ul>"""
    version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The version of the capability software that is currently running.</p>"""
    configuration: NotRequired[
        "aws_sdk_eks.types.capability_configuration_response.CapabilityConfigurationResponse"
    ]
    """<p>The configuration settings for the capability. The structure varies depending on the capability type.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    health: NotRequired["aws_sdk_eks.types.capability_health.CapabilityHealth"]
    """<p>Health information for the capability, including any issues that may be affecting its operation.</p>"""
    created_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for when the capability was created.</p>"""
    modified_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp in seconds for when the capability was last modified.</p>"""
    delete_propagation_policy: NotRequired[
        "aws_sdk_eks.types.capability_delete_propagation_policy.CapabilityDeletePropagationPolicy"
    ]
    """<p>The delete propagation policy for the capability. Currently, the only supported value is <code>RETAIN</code>, which keeps all resources managed by the capability when the capability is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Capability) -> dict:
    out: dict = {}
    if "capability_name" in value:
        out["capabilityName"] = value["capability_name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "type" in value:
        import aws_sdk_eks.types.capability_type

        out["type"] = aws_sdk_eks.types.capability_type.serialize_json(value["type"])
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "status" in value:
        import aws_sdk_eks.types.capability_status

        out["status"] = aws_sdk_eks.types.capability_status.serialize_json(
            value["status"]
        )
    if "version" in value:
        out["version"] = value["version"]
    if "configuration" in value:
        import aws_sdk_eks.types.capability_configuration_response

        out["configuration"] = (
            aws_sdk_eks.types.capability_configuration_response.serialize_json(
                value["configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    if "health" in value:
        import aws_sdk_eks.types.capability_health

        out["health"] = aws_sdk_eks.types.capability_health.serialize_json(
            value["health"]
        )
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
    if "delete_propagation_policy" in value:
        import aws_sdk_eks.types.capability_delete_propagation_policy

        out["deletePropagationPolicy"] = (
            aws_sdk_eks.types.capability_delete_propagation_policy.serialize_json(
                value["delete_propagation_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> Capability:
    out: Capability = {}  # type: ignore[typeddict-item]
    if "capabilityName" in data:
        out["capability_name"] = data["capabilityName"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "type" in data:
        import aws_sdk_eks.types.capability_type

        out["type"] = aws_sdk_eks.types.capability_type.deserialize_json(data["type"])
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "status" in data:
        import aws_sdk_eks.types.capability_status

        out["status"] = aws_sdk_eks.types.capability_status.deserialize_json(
            data["status"]
        )
    if "version" in data:
        out["version"] = data["version"]
    if "configuration" in data:
        import aws_sdk_eks.types.capability_configuration_response

        out["configuration"] = (
            aws_sdk_eks.types.capability_configuration_response.deserialize_json(
                data["configuration"]
            )
        )
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    if "health" in data:
        import aws_sdk_eks.types.capability_health

        out["health"] = aws_sdk_eks.types.capability_health.deserialize_json(
            data["health"]
        )
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
    if "deletePropagationPolicy" in data:
        import aws_sdk_eks.types.capability_delete_propagation_policy

        out["delete_propagation_policy"] = (
            aws_sdk_eks.types.capability_delete_propagation_policy.deserialize_json(
                data["deletePropagationPolicy"]
            )
        )
    return out
