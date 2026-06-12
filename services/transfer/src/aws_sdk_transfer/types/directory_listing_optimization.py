"""Generated from Smithy shape ``com.amazonaws.transfer#DirectoryListingOptimization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

"""Indicates whether optimization to directory listing on S3 servers is used. Disabled by default for compatibility."""
DirectoryListingOptimization: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: DirectoryListingOptimization) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryListingOptimization:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectoryListingOptimization value: {data!r}"
        )
    return cast(DirectoryListingOptimization, data)
