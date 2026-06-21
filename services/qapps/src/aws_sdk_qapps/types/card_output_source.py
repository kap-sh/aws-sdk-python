"""Generated from Smithy shape ``com.amazonaws.qapps#CardOutputSource``."""

from typing import Literal, TypeAlias, cast

CardOutputSource: TypeAlias = Literal[
    "approved-sources",
    "llm",
]


# --- restJson1 ser/de ---
def serialize_json(value: CardOutputSource) -> str:
    return value


def deserialize_json(data: str) -> CardOutputSource:
    return cast(CardOutputSource, data)
