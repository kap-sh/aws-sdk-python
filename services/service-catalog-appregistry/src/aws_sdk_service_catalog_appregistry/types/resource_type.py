"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "CFN_STACK",
    "RESOURCE_TAG_VALUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CFN_STACK",
        "RESOURCE_TAG_VALUE",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
