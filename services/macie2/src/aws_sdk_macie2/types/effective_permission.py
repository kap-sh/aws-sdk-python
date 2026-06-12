"""Generated from Smithy shape ``com.amazonaws.macie2#EffectivePermission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

EffectivePermission: TypeAlias = Literal[
    "PUBLIC",
    "NOT_PUBLIC",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "NOT_PUBLIC",
        "UNKNOWN",
    )
)


def serialize_json(value: EffectivePermission) -> str:
    return value


def deserialize_json(data: str) -> EffectivePermission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EffectivePermission value: {data!r}")
    return cast(EffectivePermission, data)
