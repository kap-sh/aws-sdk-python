"""Generated from Smithy shape ``com.amazonaws.kendra#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "InternalError",
    "InvalidRequest",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InternalError",
        "InvalidRequest",
    )
)


def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
