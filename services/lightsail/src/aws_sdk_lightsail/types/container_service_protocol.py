"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContainerServiceProtocol: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP",
        "HTTPS",
        "TCP",
        "UDP",
    )
)


def serialize_aws_json_1_1(value: ContainerServiceProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerServiceProtocol value: {data!r}")
    return cast(ContainerServiceProtocol, data)
