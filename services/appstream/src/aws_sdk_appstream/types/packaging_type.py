"""Generated from Smithy shape ``com.amazonaws.appstream#PackagingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

PackagingType: TypeAlias = Literal[
    "CUSTOM",
    "APPSTREAM2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM",
        "APPSTREAM2",
    )
)


def serialize_aws_json_1_1(value: PackagingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PackagingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackagingType value: {data!r}")
    return cast(PackagingType, data)
