"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentDisambiguationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.custom_disambiguation_message
    import aws_sdk_lex_models_v2.types.enabled
    import aws_sdk_lex_models_v2.types.max_disambiguation_intents


class IntentDisambiguationSettings(TypedDict, closed=True):
    enabled: "aws_sdk_lex_models_v2.types.enabled.Enabled"
    """<p>Determines whether the Intent Disambiguation feature is enabled. When set to <code>true</code>, Amazon Lex will present disambiguation options to users when multiple intents could match their input, with the default being <code>false</code>.</p>"""
    max_disambiguation_intents: NotRequired[
        "aws_sdk_lex_models_v2.types.max_disambiguation_intents.MaxDisambiguationIntents"
    ]
    """<p>Specifies the maximum number of intent options (2-5) to present to users when disambiguation is needed. This setting determines how many intent options will be shown to users when the system detects ambiguous input. The default value is 3.</p>"""
    custom_disambiguation_message: NotRequired[
        "aws_sdk_lex_models_v2.types.custom_disambiguation_message.CustomDisambiguationMessage"
    ]
    """<p>Provides a custom message that will be displayed before presenting the disambiguation options to users. This message helps set the context for users and can be customized to match your bot's tone and brand. If not specified, a default message will be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentDisambiguationSettings) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "max_disambiguation_intents" in value:
        out["maxDisambiguationIntents"] = value["max_disambiguation_intents"]
    if "custom_disambiguation_message" in value:
        out["customDisambiguationMessage"] = value["custom_disambiguation_message"]
    return out


def deserialize_json(data: dict) -> IntentDisambiguationSettings:
    out: IntentDisambiguationSettings = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "maxDisambiguationIntents" in data:
        out["max_disambiguation_intents"] = data["maxDisambiguationIntents"]
    if "customDisambiguationMessage" in data:
        out["custom_disambiguation_message"] = data["customDisambiguationMessage"]
    return out
