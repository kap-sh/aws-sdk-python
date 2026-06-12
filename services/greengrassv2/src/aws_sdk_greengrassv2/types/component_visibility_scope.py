"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentVisibilityScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

ComponentVisibilityScope: TypeAlias = Literal[
    "PRIVATE",
    "PUBLIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIVATE",
        "PUBLIC",
    )
)


def serialize_json(value: ComponentVisibilityScope) -> str:
    return value


def deserialize_json(data: str) -> ComponentVisibilityScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComponentVisibilityScope value: {data!r}")
    return cast(ComponentVisibilityScope, data)
