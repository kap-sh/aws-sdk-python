"""Generated from Smithy shape ``com.amazonaws.appsync#DefaultAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

DefaultAction: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_json(value: DefaultAction) -> str:
    return value


def deserialize_json(data: str) -> DefaultAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefaultAction value: {data!r}")
    return cast(DefaultAction, data)
