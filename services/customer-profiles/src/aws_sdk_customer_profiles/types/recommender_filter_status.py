"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderFilterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

RecommenderFilterStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING",
    "IN_PROGRESS",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PENDING",
        "IN_PROGRESS",
        "FAILED",
        "DELETING",
    )
)


def serialize_json(value: RecommenderFilterStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommenderFilterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommenderFilterStatus value: {data!r}")
    return cast(RecommenderFilterStatus, data)
