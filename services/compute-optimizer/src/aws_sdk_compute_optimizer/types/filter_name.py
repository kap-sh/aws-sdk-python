"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

FilterName: TypeAlias = Literal[
    "Finding",
    "FindingReasonCodes",
    "RecommendationSourceType",
    "InferredWorkloadTypes",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Finding",
        "FindingReasonCodes",
        "RecommendationSourceType",
        "InferredWorkloadTypes",
    )
)


def serialize_aws_json_1_0(value: FilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterName value: {data!r}")
    return cast(FilterName, data)
