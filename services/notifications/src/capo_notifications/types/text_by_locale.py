"""Generated from Smithy shape ``com.amazonaws.notifications#TextByLocale``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.locale_code

TextByLocale: TypeAlias = dict["capo_notifications.types.locale_code.LocaleCode", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TextByLocale) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TextByLocale:
    out: TextByLocale = {}
    for key, value in data.items():
        out[key] = value
    return out
