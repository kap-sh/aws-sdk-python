"""Generated from Smithy shape ``com.amazonaws.quicksight#QDataKeyType``."""

from typing import Literal, TypeAlias, cast

QDataKeyType: TypeAlias = Literal[
    "AWS_OWNED",
    "CMK",
]


# --- restJson1 ser/de ---
def serialize_json(value: QDataKeyType) -> str:
    return value


def deserialize_json(data: str) -> QDataKeyType:
    return cast(QDataKeyType, data)
