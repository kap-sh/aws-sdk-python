"""Generated from Smithy shape ``com.amazonaws.codebuild#PlatformType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

PlatformType: TypeAlias = Literal[
    "DEBIAN",
    "AMAZON_LINUX",
    "UBUNTU",
    "WINDOWS_SERVER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEBIAN",
        "AMAZON_LINUX",
        "UBUNTU",
        "WINDOWS_SERVER",
    )
)


def serialize_aws_json_1_1(value: PlatformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlatformType value: {data!r}")
    return cast(PlatformType, data)
