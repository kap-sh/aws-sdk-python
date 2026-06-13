"""Generated from Smithy shape ``com.amazonaws.inspector2#CisStringComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisStringComparison: TypeAlias = Literal[
    "EQUALS",
    "PREFIX",
    "NOT_EQUALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "PREFIX",
        "NOT_EQUALS",
    )
)


def serialize_json(value: CisStringComparison) -> str:
    return value


def deserialize_json(data: str) -> CisStringComparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisStringComparison value: {data!r}")
    return cast(CisStringComparison, data)
