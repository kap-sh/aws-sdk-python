"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssertionSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

AssertionSource: TypeAlias = Literal[
    "AI_GENERATED",
    "USER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AI_GENERATED",
        "USER",
    )
)


def serialize_json(value: AssertionSource) -> str:
    return value


def deserialize_json(data: str) -> AssertionSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssertionSource value: {data!r}")
    return cast(AssertionSource, data)
