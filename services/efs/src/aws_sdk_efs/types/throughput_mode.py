"""Generated from Smithy shape ``com.amazonaws.efs#ThroughputMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_efs.errors import DeserializationError

ThroughputMode: TypeAlias = Literal[
    "bursting",
    "provisioned",
    "elastic",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "bursting",
        "provisioned",
        "elastic",
    )
)


def serialize_json(value: ThroughputMode) -> str:
    return value


def deserialize_json(data: str) -> ThroughputMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThroughputMode value: {data!r}")
    return cast(ThroughputMode, data)
