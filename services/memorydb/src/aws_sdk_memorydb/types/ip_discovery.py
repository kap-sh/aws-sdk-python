"""Generated from Smithy shape ``com.amazonaws.memorydb#IpDiscovery``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_memorydb.errors import DeserializationError

IpDiscovery: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "ipv6",
    )
)


def serialize_aws_json_1_1(value: IpDiscovery) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpDiscovery:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpDiscovery value: {data!r}")
    return cast(IpDiscovery, data)
