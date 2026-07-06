"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#NluImprovementSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.assisted_nlu_mode
    import aws_sdk_lex_models_v2.types.enabled
    import aws_sdk_lex_models_v2.types.intent_disambiguation_settings


class NluImprovementSpecification(TypedDict, closed=True):
    enabled: "aws_sdk_lex_models_v2.types.enabled.Enabled"
    """<p>Determines whether the Assisted NLU feature is enabled for the bot. When set to <code>true</code>, Amazon Lex uses advanced models to improve intent recognition and slot resolution, with the default being <code>false</code>.</p>"""
    assisted_nlu_mode: NotRequired[
        "aws_sdk_lex_models_v2.types.assisted_nlu_mode.AssistedNluMode"
    ]
    """<p>Specifies the mode for Assisted NLU operation. Use <code>Primary</code> to make Assisted NLU the primary intent recognition method, or <code>Fallback</code> to use it only when standard NLU confidence is low.</p>"""
    intent_disambiguation_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.intent_disambiguation_settings.IntentDisambiguationSettings"
    ]
    """<p>An object containing specifications for the Intent Disambiguation feature within the Assisted NLU settings. These settings determine how the bot handles ambiguous user inputs that could match multiple intents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NluImprovementSpecification) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "assisted_nlu_mode" in value:
        import aws_sdk_lex_models_v2.types.assisted_nlu_mode

        out["assistedNluMode"] = (
            aws_sdk_lex_models_v2.types.assisted_nlu_mode.serialize_json(
                value["assisted_nlu_mode"]
            )
        )
    if "intent_disambiguation_settings" in value:
        import aws_sdk_lex_models_v2.types.intent_disambiguation_settings

        out["intentDisambiguationSettings"] = (
            aws_sdk_lex_models_v2.types.intent_disambiguation_settings.serialize_json(
                value["intent_disambiguation_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> NluImprovementSpecification:
    out: NluImprovementSpecification = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "assistedNluMode" in data:
        import aws_sdk_lex_models_v2.types.assisted_nlu_mode

        out["assisted_nlu_mode"] = (
            aws_sdk_lex_models_v2.types.assisted_nlu_mode.deserialize_json(
                data["assistedNluMode"]
            )
        )
    if "intentDisambiguationSettings" in data:
        import aws_sdk_lex_models_v2.types.intent_disambiguation_settings

        out["intent_disambiguation_settings"] = (
            aws_sdk_lex_models_v2.types.intent_disambiguation_settings.deserialize_json(
                data["intentDisambiguationSettings"]
            )
        )
    return out
