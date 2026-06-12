"""Generated from Smithy shape ``com.amazonaws.gamelift#ScalingStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ScalingStatusType: TypeAlias = Literal[
    "ACTIVE",
    "UPDATE_REQUESTED",
    "UPDATING",
    "DELETE_REQUESTED",
    "DELETING",
    "DELETED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "UPDATE_REQUESTED",
        "UPDATING",
        "DELETE_REQUESTED",
        "DELETING",
        "DELETED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: ScalingStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingStatusType value: {data!r}")
    return cast(ScalingStatusType, data)
