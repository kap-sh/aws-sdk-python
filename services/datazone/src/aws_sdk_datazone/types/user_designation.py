"""Generated from Smithy shape ``com.amazonaws.datazone#UserDesignation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

UserDesignation: TypeAlias = Literal[
    "PROJECT_OWNER",
    "PROJECT_CONTRIBUTOR",
    "PROJECT_CATALOG_VIEWER",
    "PROJECT_CATALOG_CONSUMER",
    "PROJECT_CATALOG_STEWARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROJECT_OWNER",
        "PROJECT_CONTRIBUTOR",
        "PROJECT_CATALOG_VIEWER",
        "PROJECT_CATALOG_CONSUMER",
        "PROJECT_CATALOG_STEWARD",
    )
)


def serialize_json(value: UserDesignation) -> str:
    return value


def deserialize_json(data: str) -> UserDesignation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserDesignation value: {data!r}")
    return cast(UserDesignation, data)
