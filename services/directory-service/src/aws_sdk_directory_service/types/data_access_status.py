"""Generated from Smithy shape ``com.amazonaws.directoryservice#DataAccessStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

DataAccessStatus: TypeAlias = Literal[
    "Disabled",
    "Disabling",
    "Enabled",
    "Enabling",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Disabled",
        "Disabling",
        "Enabled",
        "Enabling",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: DataAccessStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataAccessStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataAccessStatus value: {data!r}")
    return cast(DataAccessStatus, data)
