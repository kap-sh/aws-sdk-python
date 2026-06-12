"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBMetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RDSDBMetricStatistic: TypeAlias = Literal[
    "Maximum",
    "Minimum",
    "Average",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Maximum",
        "Minimum",
        "Average",
    )
)


def serialize_aws_json_1_0(value: RDSDBMetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSDBMetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RDSDBMetricStatistic value: {data!r}")
    return cast(RDSDBMetricStatistic, data)
