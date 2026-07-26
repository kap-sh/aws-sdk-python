"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#NetworkType``."""

from typing import Literal, TypeAlias, cast

"""<p>The network type of a cluster. NetworkType can be one of the following:</p> <p>IPV4: Cluster endpoints support IPv4 only.</p> <p>DUALSTACK: Cluster endpoints support both IPv4 and IPv6.</p>"""
NetworkType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkType) -> str:
    return value


def deserialize_json(data: str) -> NetworkType:
    return cast(NetworkType, data)
