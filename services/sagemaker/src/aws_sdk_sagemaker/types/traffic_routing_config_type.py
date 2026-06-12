"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrafficRoutingConfigType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrafficRoutingConfigType: TypeAlias = Literal[
    "ALL_AT_ONCE",
    "CANARY",
    "LINEAR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_AT_ONCE",
        "CANARY",
        "LINEAR",
    )
)


def serialize_aws_json_1_1(value: TrafficRoutingConfigType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrafficRoutingConfigType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrafficRoutingConfigType value: {data!r}")
    return cast(TrafficRoutingConfigType, data)
