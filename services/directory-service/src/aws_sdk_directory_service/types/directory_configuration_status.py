"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

DirectoryConfigurationStatus: TypeAlias = Literal[
    "Requested",
    "Updating",
    "Updated",
    "Failed",
    "Default",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Requested",
        "Updating",
        "Updated",
        "Failed",
        "Default",
    )
)


def serialize_aws_json_1_1(value: DirectoryConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DirectoryConfigurationStatus value: {data!r}"
        )
    return cast(DirectoryConfigurationStatus, data)
