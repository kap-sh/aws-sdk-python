"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceItemStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

ResourceItemStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "IN_PROGRESS",
    "SKIPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILED",
        "IN_PROGRESS",
        "SKIPPED",
    )
)


def serialize_json(value: ResourceItemStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceItemStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceItemStatus value: {data!r}")
    return cast(ResourceItemStatus, data)
