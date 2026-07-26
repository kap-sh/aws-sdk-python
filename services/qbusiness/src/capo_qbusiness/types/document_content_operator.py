"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentContentOperator``."""

from typing import Literal, TypeAlias, cast

DocumentContentOperator: TypeAlias = Literal["DELETE",]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContentOperator) -> str:
    return value


def deserialize_json(data: str) -> DocumentContentOperator:
    return cast(DocumentContentOperator, data)
