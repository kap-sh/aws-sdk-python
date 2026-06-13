"""Generated from Smithy shape ``com.amazonaws.odb#StandbyAllowlistedIpsSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

StandbyAllowlistedIpsSource: TypeAlias = Literal[
    "PRIMARY",
    "SEPARATE",
    "NOT_APPLICABLE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "SEPARATE",
        "NOT_APPLICABLE",
    )
)


def serialize_aws_json_1_0(value: StandbyAllowlistedIpsSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StandbyAllowlistedIpsSource:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StandbyAllowlistedIpsSource value: {data!r}"
        )
    return cast(StandbyAllowlistedIpsSource, data)
