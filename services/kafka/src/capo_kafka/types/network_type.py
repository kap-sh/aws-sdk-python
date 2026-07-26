"""Generated from Smithy shape ``com.amazonaws.kafka#NetworkType``."""

from typing import Literal, TypeAlias, cast

"""<p>The network type of the cluster, which is IPv4 or DUAL. The DUAL network type uses both IPv4 and IPv6 addresses for your cluster and its resources.</p><p>By default, a cluster uses the IPv4 network type.</p>"""
NetworkType: TypeAlias = Literal[
    "IPV4",
    "DUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkType) -> str:
    return value


def deserialize_json(data: str) -> NetworkType:
    return cast(NetworkType, data)
