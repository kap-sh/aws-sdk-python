"""Generated from Smithy shape ``com.amazonaws.elementalinference#ProfanityFilterMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elementalinference.errors import DeserializationError

ProfanityFilterMode: TypeAlias = Literal[
    "DISABLED",
    "CENSOR",
    "DROP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "CENSOR",
        "DROP",
    )
)


def serialize_json(value: ProfanityFilterMode) -> str:
    return value


def deserialize_json(data: str) -> ProfanityFilterMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfanityFilterMode value: {data!r}")
    return cast(ProfanityFilterMode, data)
