"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ConflictResolvingModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

ConflictResolvingModel: TypeAlias = Literal[
    "RECENCY",
    "SOURCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RECENCY",
        "SOURCE",
    )
)


def serialize_json(value: ConflictResolvingModel) -> str:
    return value


def deserialize_json(data: str) -> ConflictResolvingModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConflictResolvingModel value: {data!r}")
    return cast(ConflictResolvingModel, data)
