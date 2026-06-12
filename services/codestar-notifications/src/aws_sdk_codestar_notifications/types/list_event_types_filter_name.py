"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListEventTypesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_notifications.errors import DeserializationError

ListEventTypesFilterName: TypeAlias = Literal[
    "RESOURCE_TYPE",
    "SERVICE_NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE_TYPE",
        "SERVICE_NAME",
    )
)


def serialize_json(value: ListEventTypesFilterName) -> str:
    return value


def deserialize_json(data: str) -> ListEventTypesFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListEventTypesFilterName value: {data!r}")
    return cast(ListEventTypesFilterName, data)
