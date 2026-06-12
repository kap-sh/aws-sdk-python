"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_benefits.errors import DeserializationError

FileType: TypeAlias = Literal[
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/pdf",
    "image/png",
    "image/jpeg",
    "image/svg+xml",
    "text/csv",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "application/pdf",
        "image/png",
        "image/jpeg",
        "image/svg+xml",
        "text/csv",
    )
)


def serialize_aws_json_1_0(value: FileType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileType value: {data!r}")
    return cast(FileType, data)
