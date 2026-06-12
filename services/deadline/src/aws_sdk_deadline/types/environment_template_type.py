"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentTemplateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

EnvironmentTemplateType: TypeAlias = Literal[
    "JSON",
    "YAML",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "YAML",
    )
)


def serialize_json(value: EnvironmentTemplateType) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentTemplateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentTemplateType value: {data!r}")
    return cast(EnvironmentTemplateType, data)
