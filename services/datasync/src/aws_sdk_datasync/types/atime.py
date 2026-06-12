"""Generated from Smithy shape ``com.amazonaws.datasync#Atime``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

Atime: TypeAlias = Literal[
    "NONE",
    "BEST_EFFORT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "BEST_EFFORT",
    )
)


def serialize_aws_json_1_1(value: Atime) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Atime:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Atime value: {data!r}")
    return cast(Atime, data)
