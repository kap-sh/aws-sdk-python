"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ConfigChangeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

ConfigChangeStatus: TypeAlias = Literal[
    "Pending",
    "Initializing",
    "Validating",
    "ValidationFailed",
    "ApplyingChanges",
    "Completed",
    "PendingUserInput",
    "Cancelled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Initializing",
        "Validating",
        "ValidationFailed",
        "ApplyingChanges",
        "Completed",
        "PendingUserInput",
        "Cancelled",
    )
)


def serialize_json(value: ConfigChangeStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigChangeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigChangeStatus value: {data!r}")
    return cast(ConfigChangeStatus, data)
