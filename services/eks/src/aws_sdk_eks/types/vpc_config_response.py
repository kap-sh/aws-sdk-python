"""Generated from Smithy shape ``com.amazonaws.eks#VpcConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boolean
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class VpcConfigResponse(TypedDict, closed=True):
    subnet_ids: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The subnets associated with your cluster.</p>"""
    security_group_ids: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane.</p>"""
    cluster_security_group_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control-plane-to-data-plane communication.</p>"""
    vpc_id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The VPC associated with your cluster.</p>"""
    endpoint_public_access: "aws_sdk_eks.types.boolean.Boolean"
    """<p>Whether the public API server endpoint is enabled.</p>"""
    endpoint_private_access: "aws_sdk_eks.types.boolean.Boolean"
    r"""<p>This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster's VPC use the private VPC endpoint instead of traversing the internet. If this value is disabled and you have nodes or Fargate pods in the cluster, then ensure that <code>publicAccessCidrs</code> includes the necessary CIDR blocks for communication with the nodes or Fargate pods. For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html\">Cluster API server endpoint</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    public_access_cidrs: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    r"""<p>The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is <code>0.0.0.0/0</code> and additionally <code>::/0</code> for dual-stack `IPv6` clusters. If you've disabled private endpoint access, make sure that you specify the necessary CIDR blocks for every node and Fargate <code>Pod</code> in the cluster. For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html\">Cluster API server endpoint</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <p>Note that the public endpoints are dual-stack for only <code>IPv6</code> clusters that are made after October 2024. You can't add <code>IPv6</code> CIDR blocks to <code>IPv4</code> clusters or <code>IPv6</code> clusters that were made before October 2024.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigResponse) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_eks.types.string_list

        out["subnetIds"] = aws_sdk_eks.types.string_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_eks.types.string_list

        out["securityGroupIds"] = aws_sdk_eks.types.string_list.serialize_json(
            value["security_group_ids"]
        )
    if "cluster_security_group_id" in value:
        out["clusterSecurityGroupId"] = value["cluster_security_group_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    out["endpointPublicAccess"] = value.get("endpoint_public_access", False)
    out["endpointPrivateAccess"] = value.get("endpoint_private_access", False)
    if "public_access_cidrs" in value:
        import aws_sdk_eks.types.string_list

        out["publicAccessCidrs"] = aws_sdk_eks.types.string_list.serialize_json(
            value["public_access_cidrs"]
        )
    return out


def deserialize_json(data: dict) -> VpcConfigResponse:
    out: VpcConfigResponse = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_eks.types.string_list

        out["subnet_ids"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import aws_sdk_eks.types.string_list

        out["security_group_ids"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["securityGroupIds"]
        )
    if "clusterSecurityGroupId" in data:
        out["cluster_security_group_id"] = data["clusterSecurityGroupId"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "endpointPublicAccess" in data:
        out["endpoint_public_access"] = data["endpointPublicAccess"]
    else:
        out["endpoint_public_access"] = False
    if "endpointPrivateAccess" in data:
        out["endpoint_private_access"] = data["endpointPrivateAccess"]
    else:
        out["endpoint_private_access"] = False
    if "publicAccessCidrs" in data:
        import aws_sdk_eks.types.string_list

        out["public_access_cidrs"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["publicAccessCidrs"]
        )
    return out
