"""Generated from Smithy shape ``com.amazonaws.connect#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal[
    "SALESFORCE",
    "ZENDESK",
    "CASES",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceType) -> str:
    return value


def deserialize_json(data: str) -> SourceType:
    return cast(SourceType, data)
