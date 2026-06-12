"""Generated from Smithy shape ``com.amazonaws.deadline#UsageGroupByField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

UsageGroupByField: TypeAlias = Literal[
    "QUEUE_ID",
    "FLEET_ID",
    "JOB_ID",
    "USER_ID",
    "USAGE_TYPE",
    "INSTANCE_TYPE",
    "LICENSE_PRODUCT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUE_ID",
        "FLEET_ID",
        "JOB_ID",
        "USER_ID",
        "USAGE_TYPE",
        "INSTANCE_TYPE",
        "LICENSE_PRODUCT",
    )
)


def serialize_json(value: UsageGroupByField) -> str:
    return value


def deserialize_json(data: str) -> UsageGroupByField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageGroupByField value: {data!r}")
    return cast(UsageGroupByField, data)
