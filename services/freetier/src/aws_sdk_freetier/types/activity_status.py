"""Generated from Smithy shape ``com.amazonaws.freetier#ActivityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_freetier.errors import DeserializationError

ActivityStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
    "EXPIRING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "IN_PROGRESS",
        "COMPLETED",
        "EXPIRING",
    )
)


def serialize_aws_json_1_0(value: ActivityStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActivityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActivityStatus value: {data!r}")
    return cast(ActivityStatus, data)
