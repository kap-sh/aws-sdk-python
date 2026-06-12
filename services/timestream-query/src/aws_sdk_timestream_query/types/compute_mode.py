"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ComputeMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

ComputeMode: TypeAlias = Literal[
    "ON_DEMAND",
    "PROVISIONED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "PROVISIONED",
    )
)


def serialize_aws_json_1_0(value: ComputeMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComputeMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeMode value: {data!r}")
    return cast(ComputeMode, data)
