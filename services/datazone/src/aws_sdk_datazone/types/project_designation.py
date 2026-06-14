"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectDesignation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ProjectDesignation: TypeAlias = Literal[
    "OWNER",
    "CONTRIBUTOR",
    "PROJECT_CATALOG_STEWARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OWNER",
        "CONTRIBUTOR",
        "PROJECT_CATALOG_STEWARD",
    )
)


def serialize_json(value: ProjectDesignation) -> str:
    return value


def deserialize_json(data: str) -> ProjectDesignation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectDesignation value: {data!r}")
    return cast(ProjectDesignation, data)
