"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionDisplayMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormSingleSelectQuestionDisplayMode: TypeAlias = Literal[
    "DROPDOWN",
    "RADIO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DROPDOWN",
        "RADIO",
    )
)


def serialize_json(value: EvaluationFormSingleSelectQuestionDisplayMode) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormSingleSelectQuestionDisplayMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormSingleSelectQuestionDisplayMode value: {data!r}"
        )
    return cast(EvaluationFormSingleSelectQuestionDisplayMode, data)
