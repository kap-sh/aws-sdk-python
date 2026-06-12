"""Generated from Smithy shape ``com.amazonaws.datasync#Gid``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

Gid: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: Gid) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Gid:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Gid value: {data!r}")
    return cast(Gid, data)
