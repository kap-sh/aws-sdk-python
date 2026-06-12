"""Generated from Smithy shape ``com.amazonaws.b2bi#WrapFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

WrapFormat: TypeAlias = Literal[
    "SEGMENT",
    "ONE_LINE",
    "LINE_LENGTH",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEGMENT",
        "ONE_LINE",
        "LINE_LENGTH",
    )
)


def serialize_aws_json_1_0(value: WrapFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WrapFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WrapFormat value: {data!r}")
    return cast(WrapFormat, data)
