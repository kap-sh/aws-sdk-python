"""Generated from Smithy shape ``com.amazonaws.datazone#OpenLineageRunState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

OpenLineageRunState: TypeAlias = Literal[
    "START",
    "RUNNING",
    "COMPLETE",
    "ABORT",
    "FAIL",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START",
        "RUNNING",
        "COMPLETE",
        "ABORT",
        "FAIL",
        "OTHER",
    )
)


def serialize_json(value: OpenLineageRunState) -> str:
    return value


def deserialize_json(data: str) -> OpenLineageRunState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenLineageRunState value: {data!r}")
    return cast(OpenLineageRunState, data)
