"""Generated from Smithy shape ``com.amazonaws.securityhub#GranularityField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

GranularityField: TypeAlias = Literal[
    "Daily",
    "Weekly",
    "Monthly",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Daily",
        "Weekly",
        "Monthly",
    )
)


def serialize_json(value: GranularityField) -> str:
    return value


def deserialize_json(data: str) -> GranularityField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GranularityField value: {data!r}")
    return cast(GranularityField, data)
