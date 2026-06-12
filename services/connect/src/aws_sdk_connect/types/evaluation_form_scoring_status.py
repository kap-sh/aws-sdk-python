"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormScoringStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormScoringStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: EvaluationFormScoringStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormScoringStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormScoringStatus value: {data!r}"
        )
    return cast(EvaluationFormScoringStatus, data)
