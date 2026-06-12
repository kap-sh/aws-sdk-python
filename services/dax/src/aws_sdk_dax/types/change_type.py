"""Generated from Smithy shape ``com.amazonaws.dax#ChangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dax.errors import DeserializationError

ChangeType: TypeAlias = Literal[
    "IMMEDIATE",
    "REQUIRES_REBOOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMMEDIATE",
        "REQUIRES_REBOOT",
    )
)


def serialize_aws_json_1_1(value: ChangeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeType value: {data!r}")
    return cast(ChangeType, data)
