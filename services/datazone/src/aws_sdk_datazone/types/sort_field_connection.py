"""Generated from Smithy shape ``com.amazonaws.datazone#SortFieldConnection``."""

from typing import Literal, TypeAlias, cast

SortFieldConnection: TypeAlias = Literal["NAME",]


# --- restJson1 ser/de ---
def serialize_json(value: SortFieldConnection) -> str:
    return value


def deserialize_json(data: str) -> SortFieldConnection:
    return cast(SortFieldConnection, data)
