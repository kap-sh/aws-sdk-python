"""Generated from Smithy shape ``com.amazonaws.gamelift#ComputeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ComputeType: TypeAlias = Literal[
    "EC2",
    "ANYWHERE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "ANYWHERE",
    )
)


def serialize_aws_json_1_1(value: ComputeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeType value: {data!r}")
    return cast(ComputeType, data)
