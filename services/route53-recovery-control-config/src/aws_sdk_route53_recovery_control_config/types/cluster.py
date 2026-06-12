"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#Cluster``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__list_of_cluster_endpoint
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import aws_sdk_route53_recovery_control_config.types.__string_min12_max12_pattern_d12
    import aws_sdk_route53_recovery_control_config.types.network_type
    import aws_sdk_route53_recovery_control_config.types.status


class Cluster(TypedDict):
    cluster_arn: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    cluster_endpoints: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__list_of_cluster_endpoint.__listOfClusterEndpoint"
    ]
    """<p>Endpoints for a cluster. Specify one of these endpoints when you want to set or retrieve a routing control state in the cluster.</p> <p>To get or update the routing control state, see the Amazon Route 53 Application Recovery Controller Routing Control Actions.</p>"""
    name: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name of the cluster.</p>"""
    status: NotRequired["aws_sdk_route53_recovery_control_config.types.status.Status"]
    """<p>Deployment status of a resource. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</p>"""
    owner: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min12_max12_pattern_d12.__stringMin12Max12PatternD12"
    ]
    """<p>The Amazon Web Services account ID of the cluster owner.</p>"""
    network_type: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.network_type.NetworkType"
    ]
    """<p>The network type of the cluster. NetworkType can be one of the following: IPV4, DUALSTACK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cluster) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "cluster_endpoints" in value:
        import aws_sdk_route53_recovery_control_config.types.__list_of_cluster_endpoint

        out["ClusterEndpoints"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of_cluster_endpoint.serialize_json(
                value["cluster_endpoints"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_route53_recovery_control_config.types.status

        out["Status"] = (
            aws_sdk_route53_recovery_control_config.types.status.serialize_json(
                value["status"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "network_type" in value:
        import aws_sdk_route53_recovery_control_config.types.network_type

        out["NetworkType"] = (
            aws_sdk_route53_recovery_control_config.types.network_type.serialize_json(
                value["network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ClusterEndpoints" in data:
        import aws_sdk_route53_recovery_control_config.types.__list_of_cluster_endpoint

        out["cluster_endpoints"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of_cluster_endpoint.deserialize_json(
                data["ClusterEndpoints"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_route53_recovery_control_config.types.status

        out["status"] = (
            aws_sdk_route53_recovery_control_config.types.status.deserialize_json(
                data["Status"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "NetworkType" in data:
        import aws_sdk_route53_recovery_control_config.types.network_type

        out["network_type"] = (
            aws_sdk_route53_recovery_control_config.types.network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
