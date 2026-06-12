"""Generated from Smithy shape ``com.amazonaws.codebuild#ComputeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ComputeType: TypeAlias = Literal[
    "BUILD_GENERAL1_SMALL",
    "BUILD_GENERAL1_MEDIUM",
    "BUILD_GENERAL1_LARGE",
    "BUILD_GENERAL1_XLARGE",
    "BUILD_GENERAL1_2XLARGE",
    "BUILD_LAMBDA_1GB",
    "BUILD_LAMBDA_2GB",
    "BUILD_LAMBDA_4GB",
    "BUILD_LAMBDA_8GB",
    "BUILD_LAMBDA_10GB",
    "ATTRIBUTE_BASED_COMPUTE",
    "CUSTOM_INSTANCE_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUILD_GENERAL1_SMALL",
        "BUILD_GENERAL1_MEDIUM",
        "BUILD_GENERAL1_LARGE",
        "BUILD_GENERAL1_XLARGE",
        "BUILD_GENERAL1_2XLARGE",
        "BUILD_LAMBDA_1GB",
        "BUILD_LAMBDA_2GB",
        "BUILD_LAMBDA_4GB",
        "BUILD_LAMBDA_8GB",
        "BUILD_LAMBDA_10GB",
        "ATTRIBUTE_BASED_COMPUTE",
        "CUSTOM_INSTANCE_TYPE",
    )
)


def serialize_aws_json_1_1(value: ComputeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeType value: {data!r}")
    return cast(ComputeType, data)
