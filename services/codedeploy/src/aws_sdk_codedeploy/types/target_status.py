"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

TargetStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Succeeded",
    "Failed",
    "Skipped",
    "Unknown",
    "Ready",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Succeeded",
        "Failed",
        "Skipped",
        "Unknown",
        "Ready",
    )
)


def serialize_aws_json_1_1(value: TargetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetStatus value: {data!r}")
    return cast(TargetStatus, data)
