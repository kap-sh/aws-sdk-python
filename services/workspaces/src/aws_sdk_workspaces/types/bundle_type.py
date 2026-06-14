"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

BundleType: TypeAlias = Literal[
    "REGULAR",
    "STANDBY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGULAR",
        "STANDBY",
    )
)


def serialize_aws_json_1_1(value: BundleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BundleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BundleType value: {data!r}")
    return cast(BundleType, data)
