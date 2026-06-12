"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionDisplayMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormMultiSelectQuestionDisplayMode: TypeAlias = Literal[
    "DROPDOWN",
    "CHECKBOX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DROPDOWN",
        "CHECKBOX",
    )
)


def serialize_json(value: EvaluationFormMultiSelectQuestionDisplayMode) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormMultiSelectQuestionDisplayMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormMultiSelectQuestionDisplayMode value: {data!r}"
        )
    return cast(EvaluationFormMultiSelectQuestionDisplayMode, data)
