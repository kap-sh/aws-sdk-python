"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchFieldKey``."""

from typing import Literal, TypeAlias, cast

SearchFieldKey: TypeAlias = Literal["MEMBERS",]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFieldKey) -> str:
    return value


def deserialize_json(data: str) -> SearchFieldKey:
    return cast(SearchFieldKey, data)
