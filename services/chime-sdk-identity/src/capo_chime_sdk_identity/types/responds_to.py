"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#RespondsTo``."""

from typing import Literal, TypeAlias, cast

RespondsTo: TypeAlias = Literal["STANDARD_MESSAGES",]


# --- restJson1 ser/de ---
def serialize_json(value: RespondsTo) -> str:
    return value


def deserialize_json(data: str) -> RespondsTo:
    return cast(RespondsTo, data)
