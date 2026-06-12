"""Generated from Smithy shape ``com.amazonaws.securityhub#DateRangeComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

DateRangeComparison: TypeAlias = Literal[
    "WITHIN",
    "OLDER_THAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WITHIN",
        "OLDER_THAN",
    )
)


def serialize_json(value: DateRangeComparison) -> str:
    return value


def deserialize_json(data: str) -> DateRangeComparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DateRangeComparison value: {data!r}")
    return cast(DateRangeComparison, data)
