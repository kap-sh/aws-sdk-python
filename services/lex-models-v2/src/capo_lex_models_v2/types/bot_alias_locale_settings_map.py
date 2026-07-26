"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasLocaleSettingsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_locale_settings
    import capo_lex_models_v2.types.locale_id

BotAliasLocaleSettingsMap: TypeAlias = dict[
    "capo_lex_models_v2.types.locale_id.LocaleId",
    "capo_lex_models_v2.types.bot_alias_locale_settings.BotAliasLocaleSettings",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: BotAliasLocaleSettingsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_models_v2.types.bot_alias_locale_settings

        out[key] = capo_lex_models_v2.types.bot_alias_locale_settings.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> BotAliasLocaleSettingsMap:
    out: BotAliasLocaleSettingsMap = {}
    for key, value in data.items():
        import capo_lex_models_v2.types.bot_alias_locale_settings

        out[key] = capo_lex_models_v2.types.bot_alias_locale_settings.deserialize_json(
            value
        )
    return out
