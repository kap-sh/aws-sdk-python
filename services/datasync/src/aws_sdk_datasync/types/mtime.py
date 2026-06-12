"""Generated from Smithy shape ``com.amazonaws.datasync#Mtime``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

Mtime: TypeAlias = Literal[
    "NONE",
    "PRESERVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PRESERVE",
    )
)


def serialize_aws_json_1_1(value: Mtime) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Mtime:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mtime value: {data!r}")
    return cast(Mtime, data)
