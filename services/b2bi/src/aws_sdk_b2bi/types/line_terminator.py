"""Generated from Smithy shape ``com.amazonaws.b2bi#LineTerminator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

LineTerminator: TypeAlias = Literal[
    "CRLF",
    "LF",
    "CR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRLF",
        "LF",
        "CR",
    )
)


def serialize_aws_json_1_0(value: LineTerminator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LineTerminator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LineTerminator value: {data!r}")
    return cast(LineTerminator, data)
