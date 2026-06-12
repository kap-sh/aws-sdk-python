"""Generated from Smithy shape ``com.amazonaws.synthetics#RunType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_synthetics.errors import DeserializationError

RunType: TypeAlias = Literal[
    "CANARY_RUN",
    "DRY_RUN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANARY_RUN",
        "DRY_RUN",
    )
)


def serialize_json(value: RunType) -> str:
    return value


def deserialize_json(data: str) -> RunType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RunType value: {data!r}")
    return cast(RunType, data)
