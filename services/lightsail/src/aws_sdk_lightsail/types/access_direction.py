"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

AccessDirection: TypeAlias = Literal[
    "inbound",
    "outbound",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "inbound",
        "outbound",
    )
)


def serialize_aws_json_1_1(value: AccessDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessDirection value: {data!r}")
    return cast(AccessDirection, data)
