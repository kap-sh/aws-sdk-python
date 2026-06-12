"""Generated from Smithy shape ``com.amazonaws.glue#LastRefreshType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

LastRefreshType: TypeAlias = Literal[
    "FULL",
    "INCREMENTAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "INCREMENTAL",
    )
)


def serialize_aws_json_1_1(value: LastRefreshType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastRefreshType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LastRefreshType value: {data!r}")
    return cast(LastRefreshType, data)
