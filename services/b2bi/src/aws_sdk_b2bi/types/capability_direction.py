"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilityDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

CapabilityDirection: TypeAlias = Literal[
    "INBOUND",
    "OUTBOUND",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INBOUND",
        "OUTBOUND",
    )
)


def serialize_aws_json_1_0(value: CapabilityDirection) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CapabilityDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityDirection value: {data!r}")
    return cast(CapabilityDirection, data)
