"""Generated from Smithy shape ``com.amazonaws.eks#ComputeConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class ComputeConfigRequest(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Request to enable or disable the compute capability on your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your Amazon Web Services account.</p>"""
    node_pools: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>Configuration for node pools that defines the compute resources for your EKS Auto Mode cluster. For more information, see EKS Auto Mode Node Pools in the <i>Amazon EKS User Guide</i>.</p>"""
    node_role_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of the IAM Role EKS will assign to EC2 Managed Instances in your EKS Auto Mode cluster. This value cannot be changed after the compute capability of EKS Auto Mode is enabled. For more information, see the IAM Reference in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeConfigRequest) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "node_pools" in value:
        import aws_sdk_eks.types.string_list

        out["nodePools"] = aws_sdk_eks.types.string_list.serialize_json(
            value["node_pools"]
        )
    if "node_role_arn" in value:
        out["nodeRoleArn"] = value["node_role_arn"]
    return out


def deserialize_json(data: dict) -> ComputeConfigRequest:
    out: ComputeConfigRequest = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "nodePools" in data:
        import aws_sdk_eks.types.string_list

        out["node_pools"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["nodePools"]
        )
    if "nodeRoleArn" in data:
        out["node_role_arn"] = data["nodeRoleArn"]
    return out
