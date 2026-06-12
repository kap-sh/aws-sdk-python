"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

UpdateType: TypeAlias = Literal[
    "OS",
    "NETWORK",
    "SIZE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OS",
        "NETWORK",
        "SIZE",
    )
)


def serialize_aws_json_1_1(value: UpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateType value: {data!r}")
    return cast(UpdateType, data)
