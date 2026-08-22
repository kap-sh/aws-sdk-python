"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioInputLanguages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.language

AudioInputLanguages: TypeAlias = list[
    "capo_bedrock_data_automation.types.language.Language"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioInputLanguages) -> list:
    import capo_bedrock_data_automation.types.language

    out: list = []
    for item in value:
        out.append(capo_bedrock_data_automation.types.language.serialize_json(item))
    return out


def deserialize_json(data: list) -> AudioInputLanguages:
    import capo_bedrock_data_automation.types.language

    out: AudioInputLanguages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_data_automation.types.language.deserialize_json(item))
    return out
