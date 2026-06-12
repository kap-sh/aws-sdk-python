"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#Coverage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

Coverage: TypeAlias = Literal[
    "ENTIRE_ORGANIZATION",
    "MANAGEMENT_ACCOUNT_ONLY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENTIRE_ORGANIZATION",
        "MANAGEMENT_ACCOUNT_ONLY",
    )
)


def serialize_aws_json_1_0(value: Coverage) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Coverage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Coverage value: {data!r}")
    return cast(Coverage, data)
