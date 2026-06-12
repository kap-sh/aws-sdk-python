"""Generated from Smithy shape ``com.amazonaws.datasync#OverwriteMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

OverwriteMode: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS",
        "NEVER",
    )
)


def serialize_aws_json_1_1(value: OverwriteMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverwriteMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverwriteMode value: {data!r}")
    return cast(OverwriteMode, data)
