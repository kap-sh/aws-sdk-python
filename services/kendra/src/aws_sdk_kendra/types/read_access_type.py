"""Generated from Smithy shape ``com.amazonaws.kendra#ReadAccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ReadAccessType: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_1(value: ReadAccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReadAccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReadAccessType value: {data!r}")
    return cast(ReadAccessType, data)
