"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormItemEnablementAction: TypeAlias = Literal[
    "DISABLE",
    "ENABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLE",
        "ENABLE",
    )
)


def serialize_json(value: EvaluationFormItemEnablementAction) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemEnablementAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormItemEnablementAction value: {data!r}"
        )
    return cast(EvaluationFormItemEnablementAction, data)
