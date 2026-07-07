"""Generated from Smithy shape ``com.amazonaws.kafka#ServerlessConnectivityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.network_type


class ServerlessConnectivityInfo(TypedDict, closed=True):
    network_type: NotRequired["aws_sdk_kafka.types.network_type.NetworkType"]
    """<p>The network type of the cluster, which is IPv4 or DUAL. The DUAL network type uses both IPv4 and IPv6 addresses for your cluster and its resources.</p><p>By default, a cluster uses the IPv4 network type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerlessConnectivityInfo) -> dict:
    out: dict = {}
    if "network_type" in value:
        import aws_sdk_kafka.types.network_type

        out["networkType"] = aws_sdk_kafka.types.network_type.serialize_json(
            value["network_type"]
        )
    return out


def deserialize_json(data: dict) -> ServerlessConnectivityInfo:
    out: ServerlessConnectivityInfo = {}  # type: ignore[typeddict-item]
    if "networkType" in data:
        import aws_sdk_kafka.types.network_type

        out["network_type"] = aws_sdk_kafka.types.network_type.deserialize_json(
            data["networkType"]
        )
    return out
