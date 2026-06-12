"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#PartitionKeyEnforcementLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

PartitionKeyEnforcementLevel: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED",
        "OPTIONAL",
    )
)


def serialize_aws_json_1_0(value: PartitionKeyEnforcementLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PartitionKeyEnforcementLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PartitionKeyEnforcementLevel value: {data!r}"
        )
    return cast(PartitionKeyEnforcementLevel, data)
