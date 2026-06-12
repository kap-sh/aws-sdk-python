"""Generated from Smithy shape ``com.amazonaws.transfer#HomeDirectoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

HomeDirectoryType: TypeAlias = Literal[
    "PATH",
    "LOGICAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PATH",
        "LOGICAL",
    )
)


def serialize_aws_json_1_1(value: HomeDirectoryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HomeDirectoryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HomeDirectoryType value: {data!r}")
    return cast(HomeDirectoryType, data)
