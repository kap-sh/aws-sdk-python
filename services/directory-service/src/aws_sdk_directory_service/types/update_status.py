"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

UpdateStatus: TypeAlias = Literal[
    "Updated",
    "Updating",
    "UpdateFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Updated",
        "Updating",
        "UpdateFailed",
    )
)


def serialize_aws_json_1_1(value: UpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateStatus value: {data!r}")
    return cast(UpdateStatus, data)
