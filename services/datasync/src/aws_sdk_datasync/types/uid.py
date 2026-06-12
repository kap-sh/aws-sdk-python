"""Generated from Smithy shape ``com.amazonaws.datasync#Uid``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

Uid: TypeAlias = Literal[
    "NONE",
    "INT_VALUE",
    "NAME",
    "BOTH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "INT_VALUE",
        "NAME",
        "BOTH",
    )
)


def serialize_aws_json_1_1(value: Uid) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Uid:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Uid value: {data!r}")
    return cast(Uid, data)
