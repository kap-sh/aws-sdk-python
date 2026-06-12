"""Generated from Smithy shape ``com.amazonaws.codedeploy#TrafficRoutingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

TrafficRoutingType: TypeAlias = Literal[
    "TimeBasedCanary",
    "TimeBasedLinear",
    "AllAtOnce",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TimeBasedCanary",
        "TimeBasedLinear",
        "AllAtOnce",
    )
)


def serialize_aws_json_1_1(value: TrafficRoutingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrafficRoutingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrafficRoutingType value: {data!r}")
    return cast(TrafficRoutingType, data)
