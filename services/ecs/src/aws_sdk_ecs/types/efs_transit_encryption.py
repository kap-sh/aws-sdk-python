"""Generated from Smithy shape ``com.amazonaws.ecs#EFSTransitEncryption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

EFSTransitEncryption: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: EFSTransitEncryption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EFSTransitEncryption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EFSTransitEncryption value: {data!r}")
    return cast(EFSTransitEncryption, data)
