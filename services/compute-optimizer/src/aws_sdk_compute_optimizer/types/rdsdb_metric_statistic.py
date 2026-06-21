"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBMetricStatistic``."""

from typing import Literal, TypeAlias, cast

RDSDBMetricStatistic: TypeAlias = Literal[
    "Maximum",
    "Minimum",
    "Average",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBMetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSDBMetricStatistic:
    return cast(RDSDBMetricStatistic, data)
