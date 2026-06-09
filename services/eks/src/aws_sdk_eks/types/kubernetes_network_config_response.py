"""Generated from Smithy shape ``com.amazonaws.eks#KubernetesNetworkConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.elastic_load_balancing
    import aws_sdk_eks.types.ip_family
    import aws_sdk_eks.types.string


class KubernetesNetworkConfigResponse(TypedDict):
    service_ipv4_cidr: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The CIDR block that Kubernetes <code>Pod</code> and <code>Service</code> object IP addresses are assigned from. Kubernetes assigns addresses from an <code>IPv4</code> CIDR block assigned to a subnet that the node is in. If you didn't specify a CIDR block when you created the cluster, then Kubernetes assigns addresses from either the <code>10.100.0.0/16</code> or <code>172.20.0.0/16</code> CIDR blocks. If this was specified, then it was specified when the cluster was created and it can't be changed.</p>"""
    service_ipv6_cidr: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The CIDR block that Kubernetes pod and service IP addresses are assigned from if you created a 1.21 or later cluster with version 1.10.1 or later of the Amazon VPC CNI add-on and specified <code>ipv6</code> for <b>ipFamily</b> when you created the cluster. Kubernetes assigns service addresses from the unique local address range (<code>fc00::/7</code>) because you can't specify a custom IPv6 CIDR block when you create the cluster.</p>"""
    ip_family: NotRequired["aws_sdk_eks.types.ip_family.IpFamily"]
    """<p>The IP family used to assign Kubernetes <code>Pod</code> and <code>Service</code> objects IP addresses. The IP family is always <code>ipv4</code>, unless you have a <code>1.21</code> or later cluster running version <code>1.10.1</code> or later of the Amazon VPC CNI plugin for Kubernetes and specified <code>ipv6</code> when you created the cluster. </p>"""
    elastic_load_balancing: NotRequired[
        "aws_sdk_eks.types.elastic_load_balancing.ElasticLoadBalancing"
    ]
    """<p>Indicates the current configuration of the load balancing capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesNetworkConfigResponse) -> dict:
    out: dict = {}
    if "service_ipv4_cidr" in value:
        out["serviceIpv4Cidr"] = value["service_ipv4_cidr"]
    if "service_ipv6_cidr" in value:
        out["serviceIpv6Cidr"] = value["service_ipv6_cidr"]
    if "ip_family" in value:
        import aws_sdk_eks.types.ip_family

        out["ipFamily"] = aws_sdk_eks.types.ip_family.serialize_json(value["ip_family"])
    if "elastic_load_balancing" in value:
        import aws_sdk_eks.types.elastic_load_balancing

        out["elasticLoadBalancing"] = (
            aws_sdk_eks.types.elastic_load_balancing.serialize_json(
                value["elastic_load_balancing"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubernetesNetworkConfigResponse:
    out: KubernetesNetworkConfigResponse = {}  # type: ignore[typeddict-item]
    if "serviceIpv4Cidr" in data:
        out["service_ipv4_cidr"] = data["serviceIpv4Cidr"]
    if "serviceIpv6Cidr" in data:
        out["service_ipv6_cidr"] = data["serviceIpv6Cidr"]
    if "ipFamily" in data:
        import aws_sdk_eks.types.ip_family

        out["ip_family"] = aws_sdk_eks.types.ip_family.deserialize_json(
            data["ipFamily"]
        )
    if "elasticLoadBalancing" in data:
        import aws_sdk_eks.types.elastic_load_balancing

        out["elastic_load_balancing"] = (
            aws_sdk_eks.types.elastic_load_balancing.deserialize_json(
                data["elasticLoadBalancing"]
            )
        )
    return out
