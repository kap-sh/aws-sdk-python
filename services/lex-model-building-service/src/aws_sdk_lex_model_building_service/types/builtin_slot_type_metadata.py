"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BuiltinSlotTypeMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.builtin_slot_type_signature
    import aws_sdk_lex_model_building_service.types.locale_list


class BuiltinSlotTypeMetadata(TypedDict, closed=True):
    signature: NotRequired[
        "aws_sdk_lex_model_building_service.types.builtin_slot_type_signature.BuiltinSlotTypeSignature"
    ]
    r"""<p>A unique identifier for the built-in slot type. To find the signature for a slot type, see <a href=\"https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference\">Slot Type Reference</a> in the <i>Alexa Skills Kit</i>.</p>"""
    supported_locales: NotRequired[
        "aws_sdk_lex_model_building_service.types.locale_list.LocaleList"
    ]
    """<p>A list of target locales for the slot. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuiltinSlotTypeMetadata) -> dict:
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


def deserialize_json(data: dict) -> BuiltinSlotTypeMetadata:
    out: BuiltinSlotTypeMetadata = {}  # type: ignore[typeddict-item]
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
