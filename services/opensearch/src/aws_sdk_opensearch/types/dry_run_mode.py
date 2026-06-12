"""Generated from Smithy shape ``com.amazonaws.opensearch#DryRunMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

DryRunMode: TypeAlias = Literal[
    "Basic",
    "Verbose",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Basic",
        "Verbose",
    )
)


def serialize_json(value: DryRunMode) -> str:
    return value


def deserialize_json(data: str) -> DryRunMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DryRunMode value: {data!r}")
    return cast(DryRunMode, data)
