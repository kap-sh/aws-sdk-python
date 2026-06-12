"""Generated from Smithy shape ``com.amazonaws.outposts#SupportedStorageEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

SupportedStorageEnum: TypeAlias = Literal[
    "EBS",
    "S3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EBS",
        "S3",
    )
)


def serialize_json(value: SupportedStorageEnum) -> str:
    return value


def deserialize_json(data: str) -> SupportedStorageEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupportedStorageEnum value: {data!r}")
    return cast(SupportedStorageEnum, data)
