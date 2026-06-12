"""Generated from Smithy shape ``com.amazonaws.ssm#PlatformType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PlatformType: TypeAlias = Literal[
    "Windows",
    "Linux",
    "MacOS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Windows",
        "Linux",
        "MacOS",
    )
)


def serialize_aws_json_1_1(value: PlatformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlatformType value: {data!r}")
    return cast(PlatformType, data)
