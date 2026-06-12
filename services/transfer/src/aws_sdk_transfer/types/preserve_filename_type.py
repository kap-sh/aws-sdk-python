"""Generated from Smithy shape ``com.amazonaws.transfer#PreserveFilenameType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

PreserveFilenameType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: PreserveFilenameType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreserveFilenameType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreserveFilenameType value: {data!r}")
    return cast(PreserveFilenameType, data)
