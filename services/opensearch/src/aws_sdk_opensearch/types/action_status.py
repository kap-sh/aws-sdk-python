"""Generated from Smithy shape ``com.amazonaws.opensearch#ActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

ActionStatus: TypeAlias = Literal[
    "PENDING_UPDATE",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
    "NOT_ELIGIBLE",
    "ELIGIBLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_UPDATE",
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
        "NOT_ELIGIBLE",
        "ELIGIBLE",
    )
)


def serialize_json(value: ActionStatus) -> str:
    return value


def deserialize_json(data: str) -> ActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionStatus value: {data!r}")
    return cast(ActionStatus, data)
