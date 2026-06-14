"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

OperatingSystemType: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS",
        "LINUX",
    )
)


def serialize_aws_json_1_1(value: OperatingSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatingSystemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperatingSystemType value: {data!r}")
    return cast(OperatingSystemType, data)
