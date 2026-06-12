"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupPattern``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

ProtectionGroupPattern: TypeAlias = Literal[
    "ALL",
    "ARBITRARY",
    "BY_RESOURCE_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ARBITRARY",
        "BY_RESOURCE_TYPE",
    )
)


def serialize_aws_json_1_1(value: ProtectionGroupPattern) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectionGroupPattern:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtectionGroupPattern value: {data!r}")
    return cast(ProtectionGroupPattern, data)
