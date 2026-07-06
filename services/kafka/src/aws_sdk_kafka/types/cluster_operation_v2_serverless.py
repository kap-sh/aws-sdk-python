"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterOperationV2Serverless``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.serverless_connectivity_info
    import aws_sdk_kafka.types.vpc_connection_info_serverless


class ClusterOperationV2Serverless(TypedDict, closed=True):
    source_cluster_info: NotRequired[
        "aws_sdk_kafka.types.serverless_connectivity_info.ServerlessConnectivityInfo"
    ]
    """<p>Describes the cluster's attributes before any updates are applied. For example, networkType, which can be either IPv4 or DUAL.</p>"""
    target_cluster_info: NotRequired[
        "aws_sdk_kafka.types.serverless_connectivity_info.ServerlessConnectivityInfo"
    ]
    """<p>Describes the cluster's attributes after any updates are applied. For example, networkType, which can be either IPv4 or DUAL.</p>"""
    vpc_connection_info: NotRequired[
        "aws_sdk_kafka.types.vpc_connection_info_serverless.VpcConnectionInfoServerless"
    ]
    """<p>Description of the VPC connection for CreateVpcConnection and DeleteVpcConnection operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterOperationV2Serverless) -> dict:
    out: dict = {}
    if "source_cluster_info" in value:
        import aws_sdk_kafka.types.serverless_connectivity_info

        out["sourceClusterInfo"] = (
            aws_sdk_kafka.types.serverless_connectivity_info.serialize_json(
                value["source_cluster_info"]
            )
        )
    if "target_cluster_info" in value:
        import aws_sdk_kafka.types.serverless_connectivity_info

        out["targetClusterInfo"] = (
            aws_sdk_kafka.types.serverless_connectivity_info.serialize_json(
                value["target_cluster_info"]
            )
        )
    if "vpc_connection_info" in value:
        import aws_sdk_kafka.types.vpc_connection_info_serverless

        out["vpcConnectionInfo"] = (
            aws_sdk_kafka.types.vpc_connection_info_serverless.serialize_json(
                value["vpc_connection_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterOperationV2Serverless:
    out: ClusterOperationV2Serverless = {}  # type: ignore[typeddict-item]
    if "sourceClusterInfo" in data:
        import aws_sdk_kafka.types.serverless_connectivity_info

        out["source_cluster_info"] = (
            aws_sdk_kafka.types.serverless_connectivity_info.deserialize_json(
                data["sourceClusterInfo"]
            )
        )
    if "targetClusterInfo" in data:
        import aws_sdk_kafka.types.serverless_connectivity_info

        out["target_cluster_info"] = (
            aws_sdk_kafka.types.serverless_connectivity_info.deserialize_json(
                data["targetClusterInfo"]
            )
        )
    if "vpcConnectionInfo" in data:
        import aws_sdk_kafka.types.vpc_connection_info_serverless

        out["vpc_connection_info"] = (
            aws_sdk_kafka.types.vpc_connection_info_serverless.deserialize_json(
                data["vpcConnectionInfo"]
            )
        )
    return out
