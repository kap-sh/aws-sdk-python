"""Generated from Smithy shape ``com.amazonaws.applicationsignals#EvaluationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

EvaluationType: TypeAlias = Literal[
    "PeriodBased",
    "RequestBased",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PeriodBased",
        "RequestBased",
    )
)


def serialize_json(value: EvaluationType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationType value: {data!r}")
    return cast(EvaluationType, data)
