"""Generated from Smithy shape ``com.amazonaws.directoryservice#RadiusStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

RadiusStatus: TypeAlias = Literal[
    "Creating",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Completed",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: RadiusStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RadiusStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RadiusStatus value: {data!r}")
    return cast(RadiusStatus, data)
