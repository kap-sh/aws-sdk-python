"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyValueSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

PolicyValueSource: TypeAlias = Literal[
    "SELF",
    "CROSS_ACCOUNT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF",
        "CROSS_ACCOUNT",
    )
)


def serialize_json(value: PolicyValueSource) -> str:
    return value


def deserialize_json(data: str) -> PolicyValueSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyValueSource value: {data!r}")
    return cast(PolicyValueSource, data)
