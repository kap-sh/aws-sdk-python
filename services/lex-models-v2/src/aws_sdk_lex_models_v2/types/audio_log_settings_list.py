"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioLogSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.audio_log_setting

AudioLogSettingsList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.audio_log_setting.AudioLogSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioLogSettingsList) -> list:
    import aws_sdk_lex_models_v2.types.audio_log_setting

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.audio_log_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> AudioLogSettingsList:
    import aws_sdk_lex_models_v2.types.audio_log_setting

    out: AudioLogSettingsList = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.audio_log_setting.deserialize_json(item))
    return out
