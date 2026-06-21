"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobSupportedEndpointType``."""

from typing import Literal, TypeAlias, cast

RecommendationJobSupportedEndpointType: TypeAlias = Literal[
    "RealTime",
    "Serverless",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobSupportedEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationJobSupportedEndpointType:
    return cast(RecommendationJobSupportedEndpointType, data)
