"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#ConfigurationSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.word_characters_with_delimiters

ConfigurationSets: TypeAlias = list[
    "capo_pinpoint_sms_voice.types.word_characters_with_delimiters.WordCharactersWithDelimiters"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationSets) -> list:
    return list(value)


def deserialize_json(data: list) -> ConfigurationSets:
    return list(data)
