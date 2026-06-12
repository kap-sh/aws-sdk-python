"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceImportStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ResourceImportStatusType: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Failed",
        "Success",
    )
)


def serialize_json(value: ResourceImportStatusType) -> str:
    return value


def deserialize_json(data: str) -> ResourceImportStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceImportStatusType value: {data!r}")
    return cast(ResourceImportStatusType, data)
