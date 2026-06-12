"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RecommendationStepType: TypeAlias = Literal["BENCHMARK",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BENCHMARK",))


def serialize_aws_json_1_1(value: RecommendationStepType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationStepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationStepType value: {data!r}")
    return cast(RecommendationStepType, data)
