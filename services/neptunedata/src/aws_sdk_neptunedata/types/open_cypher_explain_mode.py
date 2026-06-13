"""Generated from Smithy shape ``com.amazonaws.neptunedata#OpenCypherExplainMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

OpenCypherExplainMode: TypeAlias = Literal[
    "static",
    "dynamic",
    "details",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "static",
        "dynamic",
        "details",
    )
)


def serialize_json(value: OpenCypherExplainMode) -> str:
    return value


def deserialize_json(data: str) -> OpenCypherExplainMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenCypherExplainMode value: {data!r}")
    return cast(OpenCypherExplainMode, data)
