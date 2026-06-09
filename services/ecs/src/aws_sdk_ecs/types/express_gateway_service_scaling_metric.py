"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceScalingMetric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

ExpressGatewayServiceScalingMetric: TypeAlias = Literal[
    "AVERAGE_CPU",
    "AVERAGE_MEMORY",
    "REQUEST_COUNT_PER_TARGET",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVERAGE_CPU",
        "AVERAGE_MEMORY",
        "REQUEST_COUNT_PER_TARGET",
    )
)


def serialize_aws_json_1_1(value: ExpressGatewayServiceScalingMetric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpressGatewayServiceScalingMetric:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExpressGatewayServiceScalingMetric value: {data!r}"
        )
    return cast(ExpressGatewayServiceScalingMetric, data)
