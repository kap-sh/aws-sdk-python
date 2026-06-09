"""Generated from Smithy shape ``com.amazonaws.dynamodb#WitnessStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

WitnessStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "ACTIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "ACTIVE",
    )
)


def serialize_aws_json_1_0(value: WitnessStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WitnessStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WitnessStatus value: {data!r}")
    return cast(WitnessStatus, data)
