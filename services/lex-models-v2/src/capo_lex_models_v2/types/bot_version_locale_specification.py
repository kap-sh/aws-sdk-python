"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionLocaleSpecification``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version_locale_details
    import capo_lex_models_v2.types.locale_id

BotVersionLocaleSpecification: TypeAlias = dict[
    "capo_lex_models_v2.types.locale_id.LocaleId",
    "capo_lex_models_v2.types.bot_version_locale_details.BotVersionLocaleDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: BotVersionLocaleSpecification) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_models_v2.types.bot_version_locale_details

        out[key] = capo_lex_models_v2.types.bot_version_locale_details.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> BotVersionLocaleSpecification:
    out: BotVersionLocaleSpecification = {}
    for key, value in data.items():
        import capo_lex_models_v2.types.bot_version_locale_details

        out[key] = capo_lex_models_v2.types.bot_version_locale_details.deserialize_json(
            value
        )
    return out
