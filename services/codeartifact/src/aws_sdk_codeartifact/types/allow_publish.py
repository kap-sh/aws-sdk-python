"""Generated from Smithy shape ``com.amazonaws.codeartifact#AllowPublish``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

AllowPublish: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "BLOCK",
    )
)


def serialize_json(value: AllowPublish) -> str:
    return value


def deserialize_json(data: str) -> AllowPublish:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowPublish value: {data!r}")
    return cast(AllowPublish, data)
