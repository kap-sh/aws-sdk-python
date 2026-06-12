"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobSupportedEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RecommendationJobSupportedEndpointType: TypeAlias = Literal[
    "RealTime",
    "Serverless",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RealTime",
        "Serverless",
    )
)


def serialize_aws_json_1_1(value: RecommendationJobSupportedEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationJobSupportedEndpointType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RecommendationJobSupportedEndpointType value: {data!r}"
        )
    return cast(RecommendationJobSupportedEndpointType, data)
