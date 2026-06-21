"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttributeValueOperator``."""

from typing import Literal, TypeAlias, cast

AttributeValueOperator: TypeAlias = Literal["DELETE",]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValueOperator) -> str:
    return value


def deserialize_json(data: str) -> AttributeValueOperator:
    return cast(AttributeValueOperator, data)
