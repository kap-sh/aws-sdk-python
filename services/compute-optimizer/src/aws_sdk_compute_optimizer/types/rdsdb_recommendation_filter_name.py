"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RDSDBRecommendationFilterName: TypeAlias = Literal[
    "InstanceFinding",
    "InstanceFindingReasonCode",
    "StorageFinding",
    "StorageFindingReasonCode",
    "Idle",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceFinding",
        "InstanceFindingReasonCode",
        "StorageFinding",
        "StorageFindingReasonCode",
        "Idle",
    )
)


def serialize_aws_json_1_0(value: RDSDBRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSDBRecommendationFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RDSDBRecommendationFilterName value: {data!r}"
        )
    return cast(RDSDBRecommendationFilterName, data)
