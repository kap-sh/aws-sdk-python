"""Generated from Smithy shape ``com.amazonaws.quicksight#QAResultType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

QAResultType: TypeAlias = Literal[
    "DASHBOARD_VISUAL",
    "GENERATED_ANSWER",
    "NO_ANSWER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DASHBOARD_VISUAL",
        "GENERATED_ANSWER",
        "NO_ANSWER",
    )
)


def serialize_json(value: QAResultType) -> str:
    return value


def deserialize_json(data: str) -> QAResultType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QAResultType value: {data!r}")
    return cast(QAResultType, data)
