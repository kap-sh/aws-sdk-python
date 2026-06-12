"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ResourceCategory: TypeAlias = Literal[
    "Compute",
    "Database",
    "Storage",
    "Code",
    "AI/ML",
    "Identity",
    "Network",
    "Other",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Compute",
        "Database",
        "Storage",
        "Code",
        "AI/ML",
        "Identity",
        "Network",
        "Other",
    )
)


def serialize_json(value: ResourceCategory) -> str:
    return value


def deserialize_json(data: str) -> ResourceCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceCategory value: {data!r}")
    return cast(ResourceCategory, data)
