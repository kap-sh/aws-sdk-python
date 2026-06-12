"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

PolicyType: TypeAlias = Literal[
    "AWS_MANAGED",
    "AWS_RAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_MANAGED",
        "AWS_RAM",
    )
)


def serialize_json(value: PolicyType) -> str:
    return value


def deserialize_json(data: str) -> PolicyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyType value: {data!r}")
    return cast(PolicyType, data)
