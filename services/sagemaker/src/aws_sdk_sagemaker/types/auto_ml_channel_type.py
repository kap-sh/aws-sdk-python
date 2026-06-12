"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLChannelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLChannelType: TypeAlias = Literal[
    "training",
    "validation",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "training",
        "validation",
    )
)


def serialize_aws_json_1_1(value: AutoMLChannelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLChannelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLChannelType value: {data!r}")
    return cast(AutoMLChannelType, data)
