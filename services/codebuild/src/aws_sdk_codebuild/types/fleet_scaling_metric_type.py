"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetScalingMetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetScalingMetricType: TypeAlias = Literal["FLEET_UTILIZATION_RATE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FLEET_UTILIZATION_RATE",))


def serialize_aws_json_1_1(value: FleetScalingMetricType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetScalingMetricType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetScalingMetricType value: {data!r}")
    return cast(FleetScalingMetricType, data)
