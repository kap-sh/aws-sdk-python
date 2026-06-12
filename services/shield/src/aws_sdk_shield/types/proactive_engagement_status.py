"""Generated from Smithy shape ``com.amazonaws.shield#ProactiveEngagementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

ProactiveEngagementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "PENDING",
    )
)


def serialize_aws_json_1_1(value: ProactiveEngagementStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProactiveEngagementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProactiveEngagementStatus value: {data!r}")
    return cast(ProactiveEngagementStatus, data)
