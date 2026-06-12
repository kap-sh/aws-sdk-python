"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

EnvironmentType: TypeAlias = Literal[
    "WINDOWS_CONTAINER",
    "LINUX_CONTAINER",
    "LINUX_GPU_CONTAINER",
    "ARM_CONTAINER",
    "WINDOWS_SERVER_2019_CONTAINER",
    "WINDOWS_SERVER_2022_CONTAINER",
    "LINUX_LAMBDA_CONTAINER",
    "ARM_LAMBDA_CONTAINER",
    "LINUX_EC2",
    "ARM_EC2",
    "WINDOWS_EC2",
    "MAC_ARM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS_CONTAINER",
        "LINUX_CONTAINER",
        "LINUX_GPU_CONTAINER",
        "ARM_CONTAINER",
        "WINDOWS_SERVER_2019_CONTAINER",
        "WINDOWS_SERVER_2022_CONTAINER",
        "LINUX_LAMBDA_CONTAINER",
        "ARM_LAMBDA_CONTAINER",
        "LINUX_EC2",
        "ARM_EC2",
        "WINDOWS_EC2",
        "MAC_ARM",
    )
)


def serialize_aws_json_1_1(value: EnvironmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentType value: {data!r}")
    return cast(EnvironmentType, data)
