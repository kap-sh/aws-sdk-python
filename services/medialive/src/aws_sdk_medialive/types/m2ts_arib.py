"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsArib``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Arib"""
M2tsArib: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: M2tsArib) -> str:
    return value


def deserialize_json(data: str) -> M2tsArib:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsArib value: {data!r}")
    return cast(M2tsArib, data)
