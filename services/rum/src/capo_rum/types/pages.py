"""Generated from Smithy shape ``com.amazonaws.rum#Pages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.url

Pages: TypeAlias = list["capo_rum.types.url.Url"]


# --- restJson1 ser/de ---
def serialize_json(value: Pages) -> list:
    return list(value)


def deserialize_json(data: list) -> Pages:
    return list(data)
