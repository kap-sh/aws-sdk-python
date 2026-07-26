"""Generated from Smithy shape ``com.amazonaws.connect#NotificationContent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.locale_code
    import capo_connect.types.localized_string

NotificationContent: TypeAlias = dict[
    "capo_connect.types.locale_code.LocaleCode",
    "capo_connect.types.localized_string.LocalizedString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: NotificationContent) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect.types.locale_code

        out[capo_connect.types.locale_code.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> NotificationContent:
    out: NotificationContent = {}
    for key, value in data.items():
        import capo_connect.types.locale_code

        out[capo_connect.types.locale_code.deserialize_json(key)] = value
    return out
