"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceAccessProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

InstanceAccessProtocol: TypeAlias = Literal[
    "ssh",
    "rdp",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ssh",
        "rdp",
    )
)


def serialize_aws_json_1_1(value: InstanceAccessProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceAccessProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceAccessProtocol value: {data!r}")
    return cast(InstanceAccessProtocol, data)
