"""Generated from Smithy shape ``com.amazonaws.workspaces#OSVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

OSVersion: TypeAlias = Literal[
    "Windows_10",
    "Windows_11",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Windows_10",
        "Windows_11",
    )
)


def serialize_aws_json_1_1(value: OSVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OSVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OSVersion value: {data!r}")
    return cast(OSVersion, data)
