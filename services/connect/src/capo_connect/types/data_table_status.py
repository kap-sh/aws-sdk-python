"""Generated from Smithy shape ``com.amazonaws.connect#DataTableStatus``."""

from typing import Literal, TypeAlias, cast

DataTableStatus: TypeAlias = Literal["PUBLISHED",]


# --- restJson1 ser/de ---
def serialize_json(value: DataTableStatus) -> str:
    return value


def deserialize_json(data: str) -> DataTableStatus:
    return cast(DataTableStatus, data)
