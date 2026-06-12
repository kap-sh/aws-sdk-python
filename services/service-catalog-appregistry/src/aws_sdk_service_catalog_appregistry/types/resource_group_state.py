"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceGroupState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

ResourceGroupState: TypeAlias = Literal[
    "CREATING",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "UPDATING",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
    )
)


def serialize_json(value: ResourceGroupState) -> str:
    return value


def deserialize_json(data: str) -> ResourceGroupState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceGroupState value: {data!r}")
    return cast(ResourceGroupState, data)
