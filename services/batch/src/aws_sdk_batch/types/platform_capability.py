"""Generated from Smithy shape ``com.amazonaws.batch#PlatformCapability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

PlatformCapability: TypeAlias = Literal[
    "EC2",
    "FARGATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "FARGATE",
    )
)


def serialize_json(value: PlatformCapability) -> str:
    return value


def deserialize_json(data: str) -> PlatformCapability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlatformCapability value: {data!r}")
    return cast(PlatformCapability, data)
