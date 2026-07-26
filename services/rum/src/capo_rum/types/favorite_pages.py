"""Generated from Smithy shape ``com.amazonaws.rum#FavoritePages``."""

from typing import TypeAlias

FavoritePages: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: FavoritePages) -> list:
    return list(value)


def deserialize_json(data: list) -> FavoritePages:
    return list(data)
