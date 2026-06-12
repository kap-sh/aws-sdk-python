"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemSourceValuesComparator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormItemSourceValuesComparator: TypeAlias = Literal[
    "IN",
    "NOT_IN",
    "ALL_IN",
    "EXACT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN",
        "NOT_IN",
        "ALL_IN",
        "EXACT",
    )
)


def serialize_json(value: EvaluationFormItemSourceValuesComparator) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemSourceValuesComparator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormItemSourceValuesComparator value: {data!r}"
        )
    return cast(EvaluationFormItemSourceValuesComparator, data)
