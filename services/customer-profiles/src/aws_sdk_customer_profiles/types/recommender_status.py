"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

RecommenderStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "ACTIVE",
    "FAILED",
    "STOPPING",
    "INACTIVE",
    "STARTING",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "ACTIVE",
        "FAILED",
        "STOPPING",
        "INACTIVE",
        "STARTING",
        "DELETING",
    )
)


def serialize_json(value: RecommenderStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommenderStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommenderStatus value: {data!r}")
    return cast(RecommenderStatus, data)
