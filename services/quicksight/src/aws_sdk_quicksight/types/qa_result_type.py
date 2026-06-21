"""Generated from Smithy shape ``com.amazonaws.quicksight#QAResultType``."""

from typing import Literal, TypeAlias, cast

QAResultType: TypeAlias = Literal[
    "DASHBOARD_VISUAL",
    "GENERATED_ANSWER",
    "NO_ANSWER",
]


# --- restJson1 ser/de ---
def serialize_json(value: QAResultType) -> str:
    return value


def deserialize_json(data: str) -> QAResultType:
    return cast(QAResultType, data)
