"""Generated from Smithy shape ``com.amazonaws.opensearch#RequirementLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

RequirementLevel: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED",
        "OPTIONAL",
        "NONE",
    )
)


def serialize_json(value: RequirementLevel) -> str:
    return value


def deserialize_json(data: str) -> RequirementLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RequirementLevel value: {data!r}")
    return cast(RequirementLevel, data)
