"""Generated from Smithy shape ``com.amazonaws.wafv2#LowReputationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

LowReputationMode: TypeAlias = Literal[
    "ACTIVE_UNDER_DDOS",
    "ALWAYS_ON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE_UNDER_DDOS",
        "ALWAYS_ON",
    )
)


def serialize_aws_json_1_1(value: LowReputationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LowReputationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LowReputationMode value: {data!r}")
    return cast(LowReputationMode, data)
