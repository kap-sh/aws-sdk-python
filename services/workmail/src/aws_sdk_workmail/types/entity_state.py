"""Generated from Smithy shape ``com.amazonaws.workmail#EntityState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

EntityState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: EntityState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityState value: {data!r}")
    return cast(EntityState, data)
