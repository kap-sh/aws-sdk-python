"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetPlatformOs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TargetPlatformOs: TypeAlias = Literal[
    "ANDROID",
    "LINUX",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANDROID",
        "LINUX",
    )
)


def serialize_aws_json_1_1(value: TargetPlatformOs) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetPlatformOs:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetPlatformOs value: {data!r}")
    return cast(TargetPlatformOs, data)
