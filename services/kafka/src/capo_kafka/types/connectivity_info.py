"""Generated from Smithy shape ``com.amazonaws.kafka#ConnectivityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.network_type
    import capo_kafka.types.public_access
    import capo_kafka.types.vpc_connectivity


class ConnectivityInfo(TypedDict, closed=True):
    public_access: NotRequired["capo_kafka.types.public_access.PublicAccess"]
    """<p>Public access control for brokers.</p>"""
    vpc_connectivity: NotRequired["capo_kafka.types.vpc_connectivity.VpcConnectivity"]
    """<p>VPC connectivity access control for brokers.</p>"""
    network_type: NotRequired["capo_kafka.types.network_type.NetworkType"]
    """<p>The network type of the cluster, which is IPv4 or DUAL. The DUAL network type uses both IPv4 and IPv6 addresses for your cluster and its resources.</p><p>By default, a cluster uses the IPv4 network type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectivityInfo) -> dict:
    out: dict = {}
    if "public_access" in value:
        import capo_kafka.types.public_access

        out["publicAccess"] = capo_kafka.types.public_access.serialize_json(
            value["public_access"]
        )
    if "vpc_connectivity" in value:
        import capo_kafka.types.vpc_connectivity

        out["vpcConnectivity"] = capo_kafka.types.vpc_connectivity.serialize_json(
            value["vpc_connectivity"]
        )
    if "network_type" in value:
        import capo_kafka.types.network_type

        out["networkType"] = capo_kafka.types.network_type.serialize_json(
            value["network_type"]
        )
    return out


def deserialize_json(data: dict) -> ConnectivityInfo:
    out: ConnectivityInfo = {}  # type: ignore[typeddict-item]
    if "publicAccess" in data:
        import capo_kafka.types.public_access

        out["public_access"] = capo_kafka.types.public_access.deserialize_json(
            data["publicAccess"]
        )
    if "vpcConnectivity" in data:
        import capo_kafka.types.vpc_connectivity

        out["vpc_connectivity"] = capo_kafka.types.vpc_connectivity.deserialize_json(
            data["vpcConnectivity"]
        )
    if "networkType" in data:
        import capo_kafka.types.network_type

        out["network_type"] = capo_kafka.types.network_type.deserialize_json(
            data["networkType"]
        )
    return out
