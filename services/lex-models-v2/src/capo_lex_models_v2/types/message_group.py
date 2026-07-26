"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#MessageGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.message
    import capo_lex_models_v2.types.message_variations_list


class MessageGroup(TypedDict, closed=True):
    message: "capo_lex_models_v2.types.message.Message"
    """<p>The primary message that Amazon Lex should send to the user.</p>"""
    variations: NotRequired[
        "capo_lex_models_v2.types.message_variations_list.MessageVariationsList"
    ]
    """<p>Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageGroup) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.message

    out["message"] = capo_lex_models_v2.types.message.serialize_json(value["message"])
    if "variations" in value:
        import capo_lex_models_v2.types.message_variations_list

        out["variations"] = (
            capo_lex_models_v2.types.message_variations_list.serialize_json(
                value["variations"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageGroup:
    out: MessageGroup = {}  # type: ignore[typeddict-item]
    if "message" in data:
        import capo_lex_models_v2.types.message

        out["message"] = capo_lex_models_v2.types.message.deserialize_json(
            data["message"]
        )
    else:
        raise DeserializationError("MessageGroup.message required")
    if "variations" in data:
        import capo_lex_models_v2.types.message_variations_list

        out["variations"] = (
            capo_lex_models_v2.types.message_variations_list.deserialize_json(
                data["variations"]
            )
        )
    return out
