"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

PolicyStatus: TypeAlias = Literal[
    "ATTACHABLE",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTACHABLE",
        "DEPRECATED",
    )
)


def serialize_json(value: PolicyStatus) -> str:
    return value


def deserialize_json(data: str) -> PolicyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyStatus value: {data!r}")
    return cast(PolicyStatus, data)
