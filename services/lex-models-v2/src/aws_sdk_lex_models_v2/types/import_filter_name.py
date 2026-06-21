"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportFilterName``."""

from typing import Literal, TypeAlias, cast

ImportFilterName: TypeAlias = Literal["ImportResourceType",]


# --- restJson1 ser/de ---
def serialize_json(value: ImportFilterName) -> str:
    return value


def deserialize_json(data: str) -> ImportFilterName:
    return cast(ImportFilterName, data)
