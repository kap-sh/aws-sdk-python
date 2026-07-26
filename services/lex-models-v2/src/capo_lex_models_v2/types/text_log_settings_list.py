"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TextLogSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.text_log_setting

TextLogSettingsList: TypeAlias = list[
    "capo_lex_models_v2.types.text_log_setting.TextLogSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: TextLogSettingsList) -> list:
    import capo_lex_models_v2.types.text_log_setting

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.text_log_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> TextLogSettingsList:
    import capo_lex_models_v2.types.text_log_setting

    out: TextLogSettingsList = []
    for item in data:
        out.append(capo_lex_models_v2.types.text_log_setting.deserialize_json(item))
    return out
