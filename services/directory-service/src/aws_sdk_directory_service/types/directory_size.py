"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectorySize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

DirectorySize: TypeAlias = Literal[
    "Small",
    "Large",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Small",
        "Large",
    )
)


def serialize_aws_json_1_1(value: DirectorySize) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectorySize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DirectorySize value: {data!r}")
    return cast(DirectorySize, data)
