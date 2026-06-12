"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSCurrentInstancePerformanceRisk``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RDSCurrentInstancePerformanceRisk: TypeAlias = Literal[
    "VeryLow",
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VeryLow",
        "Low",
        "Medium",
        "High",
    )
)


def serialize_aws_json_1_0(value: RDSCurrentInstancePerformanceRisk) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSCurrentInstancePerformanceRisk:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RDSCurrentInstancePerformanceRisk value: {data!r}"
        )
    return cast(RDSCurrentInstancePerformanceRisk, data)
