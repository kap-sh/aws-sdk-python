"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BuiltinIntentMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.builtin_intent_signature
    import aws_sdk_lex_model_building_service.types.locale_list


class BuiltinIntentMetadata(TypedDict):
    signature: NotRequired[
        "aws_sdk_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature"
    ]
    """<p>A unique identifier for the built-in intent. To find the signature for an intent, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>"""
    supported_locales: NotRequired[
        "aws_sdk_lex_model_building_service.types.locale_list.LocaleList"
    ]
    """<p>A list of identifiers for the locales that the intent supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuiltinIntentMetadata) -> dict:
    out: dict = {}
    if "signature" in value:
        out["signature"] = value["signature"]
    if "supported_locales" in value:
        import aws_sdk_lex_model_building_service.types.locale_list

        out["supportedLocales"] = (
            aws_sdk_lex_model_building_service.types.locale_list.serialize_json(
                value["supported_locales"]
            )
        )
    return out


def deserialize_json(data: dict) -> BuiltinIntentMetadata:
    out: BuiltinIntentMetadata = {}  # type: ignore[typeddict-item]
    if "signature" in data:
        out["signature"] = data["signature"]
    if "supportedLocales" in data:
        import aws_sdk_lex_model_building_service.types.locale_list

        out["supported_locales"] = (
            aws_sdk_lex_model_building_service.types.locale_list.deserialize_json(
                data["supportedLocales"]
            )
        )
    return out
