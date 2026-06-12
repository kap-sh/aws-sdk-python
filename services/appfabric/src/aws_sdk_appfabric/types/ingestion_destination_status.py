"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionDestinationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

IngestionDestinationStatus: TypeAlias = Literal[
    "Active",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Failed",
    )
)


def serialize_json(value: IngestionDestinationStatus) -> str:
    return value


def deserialize_json(data: str) -> IngestionDestinationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngestionDestinationStatus value: {data!r}"
        )
    return cast(IngestionDestinationStatus, data)
