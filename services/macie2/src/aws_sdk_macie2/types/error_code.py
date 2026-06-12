"""Generated from Smithy shape ``com.amazonaws.macie2#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The source of an issue or delay. Possible values are:</p>"""
ErrorCode: TypeAlias = Literal[
    "ClientError",
    "InternalError",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ClientError",
        "InternalError",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
