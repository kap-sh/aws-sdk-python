"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSourceValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormItemEnablementSourceValueType: TypeAlias = Literal["OPTION_REF_ID",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OPTION_REF_ID",))


def serialize_json(value: EvaluationFormItemEnablementSourceValueType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemEnablementSourceValueType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormItemEnablementSourceValueType value: {data!r}"
        )
    return cast(EvaluationFormItemEnablementSourceValueType, data)
