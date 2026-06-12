"""Generated from Smithy shape ``com.amazonaws.devicefarm#UploadCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

UploadCategory: TypeAlias = Literal[
    "CURATED",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURATED",
        "PRIVATE",
    )
)


def serialize_aws_json_1_1(value: UploadCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UploadCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UploadCategory value: {data!r}")
    return cast(UploadCategory, data)
