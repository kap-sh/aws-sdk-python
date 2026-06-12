"""Generated from Smithy shape ``com.amazonaws.transfer#OverwriteExisting``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

OverwriteExisting: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
    )
)


def serialize_aws_json_1_1(value: OverwriteExisting) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverwriteExisting:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverwriteExisting value: {data!r}")
    return cast(OverwriteExisting, data)
