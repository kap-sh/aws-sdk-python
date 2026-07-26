"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLogSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.audio_log_settings_list
    import capo_lex_models_v2.types.text_log_settings_list


class ConversationLogSettings(TypedDict, closed=True):
    text_log_settings: NotRequired[
        "capo_lex_models_v2.types.text_log_settings_list.TextLogSettingsList"
    ]
    """<p>The Amazon CloudWatch Logs settings for logging text and metadata.</p>"""
    audio_log_settings: NotRequired[
        "capo_lex_models_v2.types.audio_log_settings_list.AudioLogSettingsList"
    ]
    """<p>The Amazon S3 settings for logging audio to an S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLogSettings) -> dict:
    out: dict = {}
    if "text_log_settings" in value:
        import capo_lex_models_v2.types.text_log_settings_list

        out["textLogSettings"] = (
            capo_lex_models_v2.types.text_log_settings_list.serialize_json(
                value["text_log_settings"]
            )
        )
    if "audio_log_settings" in value:
        import capo_lex_models_v2.types.audio_log_settings_list

        out["audioLogSettings"] = (
            capo_lex_models_v2.types.audio_log_settings_list.serialize_json(
                value["audio_log_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConversationLogSettings:
    out: ConversationLogSettings = {}  # type: ignore[typeddict-item]
    if "textLogSettings" in data:
        import capo_lex_models_v2.types.text_log_settings_list

        out["text_log_settings"] = (
            capo_lex_models_v2.types.text_log_settings_list.deserialize_json(
                data["textLogSettings"]
            )
        )
    if "audioLogSettings" in data:
        import capo_lex_models_v2.types.audio_log_settings_list

        out["audio_log_settings"] = (
            capo_lex_models_v2.types.audio_log_settings_list.deserialize_json(
                data["audioLogSettings"]
            )
        )
    return out
