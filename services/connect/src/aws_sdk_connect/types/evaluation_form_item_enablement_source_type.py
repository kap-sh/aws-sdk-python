"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormItemEnablementSourceType: TypeAlias = Literal["QUESTION_REF_ID",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("QUESTION_REF_ID",))


def serialize_json(value: EvaluationFormItemEnablementSourceType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemEnablementSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormItemEnablementSourceType value: {data!r}"
        )
    return cast(EvaluationFormItemEnablementSourceType, data)
