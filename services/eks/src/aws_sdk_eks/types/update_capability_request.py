"""Generated from Smithy shape ``com.amazonaws.eks#UpdateCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.capability_delete_propagation_policy
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.update_capability_configuration


class UpdateCapabilityRequest(TypedDict, closed=True):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster that contains the capability you want to update configuration for.</p>"""
    capability_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the capability to update configuration for.</p>"""
    role_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the capability uses to interact with Amazon Web Services services. If you specify a new role ARN, the capability will start using the new role for all subsequent operations.</p>"""
    configuration: NotRequired[
        "aws_sdk_eks.types.update_capability_configuration.UpdateCapabilityConfiguration"
    ]
    """<p>The updated configuration settings for the capability. You only need to specify the configuration parameters you want to change. For Argo CD capabilities, you can update RBAC role mappings and network access settings.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is valid for 24 hours after creation.</p>"""
    delete_propagation_policy: NotRequired[
        "aws_sdk_eks.types.capability_delete_propagation_policy.CapabilityDeletePropagationPolicy"
    ]
    """<p>The updated delete propagation policy for the capability. Currently, the only supported value is <code>RETAIN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCapabilityRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "configuration" in value:
        import aws_sdk_eks.types.update_capability_configuration

        out["configuration"] = (
            aws_sdk_eks.types.update_capability_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "delete_propagation_policy" in value:
        import aws_sdk_eks.types.capability_delete_propagation_policy

        out["deletePropagationPolicy"] = (
            aws_sdk_eks.types.capability_delete_propagation_policy.serialize_json(
                value["delete_propagation_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCapabilityRequest:
    out: UpdateCapabilityRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "configuration" in data:
        import aws_sdk_eks.types.update_capability_configuration

        out["configuration"] = (
            aws_sdk_eks.types.update_capability_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "deletePropagationPolicy" in data:
        import aws_sdk_eks.types.capability_delete_propagation_policy

        out["delete_propagation_policy"] = (
            aws_sdk_eks.types.capability_delete_propagation_policy.deserialize_json(
                data["deletePropagationPolicy"]
            )
        )
    return out
