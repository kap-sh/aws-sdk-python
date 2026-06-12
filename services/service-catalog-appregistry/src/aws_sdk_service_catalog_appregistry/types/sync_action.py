"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#SyncAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

SyncAction: TypeAlias = Literal[
    "START_SYNC",
    "NO_ACTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_SYNC",
        "NO_ACTION",
    )
)


def serialize_json(value: SyncAction) -> str:
    return value


def deserialize_json(data: str) -> SyncAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SyncAction value: {data!r}")
    return cast(SyncAction, data)
