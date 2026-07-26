"""Generated from Smithy shape ``com.amazonaws.glacier#ExpressionType``."""

from typing import Literal, TypeAlias, cast

ExpressionType: TypeAlias = Literal["SQL",]


# --- restJson1 ser/de ---
def serialize_json(value: ExpressionType) -> str:
    return value


def deserialize_json(data: str) -> ExpressionType:
    return cast(ExpressionType, data)
