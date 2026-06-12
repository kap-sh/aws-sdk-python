"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

DirectoryType: TypeAlias = Literal[
    "SimpleAD",
    "ADConnector",
    "MicrosoftAD",
    "SharedMicrosoftAD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SimpleAD",
        "ADConnector",
        "MicrosoftAD",
        "SharedMicrosoftAD",
    )
)


def serialize_aws_json_1_1(value: DirectoryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DirectoryType value: {data!r}")
    return cast(DirectoryType, data)
