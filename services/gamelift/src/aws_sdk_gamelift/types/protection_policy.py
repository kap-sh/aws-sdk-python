"""Generated from Smithy shape ``com.amazonaws.gamelift#ProtectionPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ProtectionPolicy: TypeAlias = Literal[
    "NoProtection",
    "FullProtection",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NoProtection",
        "FullProtection",
    )
)


def serialize_aws_json_1_1(value: ProtectionPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectionPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtectionPolicy value: {data!r}")
    return cast(ProtectionPolicy, data)
