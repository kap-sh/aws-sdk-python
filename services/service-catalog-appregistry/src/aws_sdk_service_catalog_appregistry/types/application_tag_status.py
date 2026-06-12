"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ApplicationTagStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

ApplicationTagStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESS",
        "FAILURE",
    )
)


def serialize_json(value: ApplicationTagStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationTagStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationTagStatus value: {data!r}")
    return cast(ApplicationTagStatus, data)
