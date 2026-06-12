"""Generated from Smithy shape ``com.amazonaws.directoryservice#OSVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

OSVersion: TypeAlias = Literal[
    "SERVER_2012",
    "SERVER_2019",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVER_2012",
        "SERVER_2019",
    )
)


def serialize_aws_json_1_1(value: OSVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OSVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OSVersion value: {data!r}")
    return cast(OSVersion, data)
