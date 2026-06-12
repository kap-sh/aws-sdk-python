"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormItemEnablementOperator: TypeAlias = Literal[
    "OR",
    "AND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OR",
        "AND",
    )
)


def serialize_json(value: EvaluationFormItemEnablementOperator) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemEnablementOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormItemEnablementOperator value: {data!r}"
        )
    return cast(EvaluationFormItemEnablementOperator, data)
