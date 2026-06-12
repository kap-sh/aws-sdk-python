"""Generated from Smithy shape ``com.amazonaws.fsx#DiskIopsConfigurationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

DiskIopsConfigurationMode: TypeAlias = Literal[
    "AUTOMATIC",
    "USER_PROVISIONED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "USER_PROVISIONED",
    )
)


def serialize_aws_json_1_1(value: DiskIopsConfigurationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiskIopsConfigurationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiskIopsConfigurationMode value: {data!r}")
    return cast(DiskIopsConfigurationMode, data)
