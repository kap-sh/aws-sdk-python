"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormVersionStatus: TypeAlias = Literal[
    "DRAFT",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "ACTIVE",
    )
)


def serialize_json(value: EvaluationFormVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormVersionStatus value: {data!r}"
        )
    return cast(EvaluationFormVersionStatus, data)
