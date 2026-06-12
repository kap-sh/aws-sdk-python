"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#NetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53_recovery_control_config.errors import DeserializationError

"""<p>The network type of a cluster. NetworkType can be one of the following:</p> <p>IPV4: Cluster endpoints support IPv4 only.</p> <p>DUALSTACK: Cluster endpoints support both IPv4 and IPv6.</p>"""
NetworkType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUALSTACK",
    )
)


def serialize_json(value: NetworkType) -> str:
    return value


def deserialize_json(data: str) -> NetworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkType value: {data!r}")
    return cast(NetworkType, data)
