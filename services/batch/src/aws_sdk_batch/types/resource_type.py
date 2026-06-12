"""Generated from Smithy shape ``com.amazonaws.batch#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "GPU",
    "VCPU",
    "MEMORY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GPU",
        "VCPU",
        "MEMORY",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
