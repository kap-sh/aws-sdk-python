"""Generated from Smithy shape ``com.amazonaws.sagemaker#SharingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SharingType: TypeAlias = Literal[
    "Private",
    "Shared",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Private",
        "Shared",
    )
)


def serialize_aws_json_1_1(value: SharingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SharingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SharingType value: {data!r}")
    return cast(SharingType, data)
