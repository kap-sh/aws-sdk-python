"""Generated from Smithy shape ``com.amazonaws.securityhub#StringFilterComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

StringFilterComparison: TypeAlias = Literal[
    "EQUALS",
    "PREFIX",
    "NOT_EQUALS",
    "PREFIX_NOT_EQUALS",
    "CONTAINS",
    "NOT_CONTAINS",
    "CONTAINS_WORD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "PREFIX",
        "NOT_EQUALS",
        "PREFIX_NOT_EQUALS",
        "CONTAINS",
        "NOT_CONTAINS",
        "CONTAINS_WORD",
    )
)


def serialize_json(value: StringFilterComparison) -> str:
    return value


def deserialize_json(data: str) -> StringFilterComparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StringFilterComparison value: {data!r}")
    return cast(StringFilterComparison, data)
