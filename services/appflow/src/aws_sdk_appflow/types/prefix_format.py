"""Generated from Smithy shape ``com.amazonaws.appflow#PrefixFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

PrefixFormat: TypeAlias = Literal[
    "YEAR",
    "MONTH",
    "DAY",
    "HOUR",
    "MINUTE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "YEAR",
        "MONTH",
        "DAY",
        "HOUR",
        "MINUTE",
    )
)


def serialize_json(value: PrefixFormat) -> str:
    return value


def deserialize_json(data: str) -> PrefixFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrefixFormat value: {data!r}")
    return cast(PrefixFormat, data)
