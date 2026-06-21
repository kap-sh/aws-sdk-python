"""Generated from Smithy shape ``com.amazonaws.transfer#DirectoryListingOptimization``."""

from typing import Literal, TypeAlias, cast

"""Indicates whether optimization to directory listing on S3 servers is used. Disabled by default for compatibility."""
DirectoryListingOptimization: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryListingOptimization) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryListingOptimization:
    return cast(DirectoryListingOptimization, data)
