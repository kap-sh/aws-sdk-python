"""Generated from Smithy shape ``com.amazonaws.macie2#EffectivePermission``."""

from typing import Literal, TypeAlias, cast

EffectivePermission: TypeAlias = Literal[
    "PUBLIC",
    "NOT_PUBLIC",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectivePermission) -> str:
    return value


def deserialize_json(data: str) -> EffectivePermission:
    return cast(EffectivePermission, data)
