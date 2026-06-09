"""Generated from Smithy shape ``com.amazonaws.ecs#TransportProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

TransportProtocol: TypeAlias = Literal[
    "tcp",
    "udp",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "tcp",
        "udp",
    )
)


def serialize_aws_json_1_1(value: TransportProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransportProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransportProtocol value: {data!r}")
    return cast(TransportProtocol, data)
