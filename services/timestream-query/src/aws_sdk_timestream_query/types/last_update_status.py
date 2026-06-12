"""Generated from Smithy shape ``com.amazonaws.timestreamquery#LastUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

LastUpdateStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "SUCCEEDED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "FAILED",
        "SUCCEEDED",
    )
)


def serialize_aws_json_1_0(value: LastUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LastUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastUpdateStatus value: {data!r}")
    return cast(LastUpdateStatus, data)
