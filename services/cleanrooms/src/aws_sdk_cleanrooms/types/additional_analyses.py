"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AdditionalAnalyses``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AdditionalAnalyses: TypeAlias = Literal[
    "ALLOWED",
    "REQUIRED",
    "NOT_ALLOWED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOWED",
        "REQUIRED",
        "NOT_ALLOWED",
    )
)


def serialize_json(value: AdditionalAnalyses) -> str:
    return value


def deserialize_json(data: str) -> AdditionalAnalyses:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdditionalAnalyses value: {data!r}")
    return cast(AdditionalAnalyses, data)
