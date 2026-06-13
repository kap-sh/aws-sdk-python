"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Trace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

Trace: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLED_FULL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "ENABLED_FULL",
    )
)


def serialize_json(value: Trace) -> str:
    return value


def deserialize_json(data: str) -> Trace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Trace value: {data!r}")
    return cast(Trace, data)
