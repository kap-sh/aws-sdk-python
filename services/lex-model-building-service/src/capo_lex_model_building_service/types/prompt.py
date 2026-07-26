"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Prompt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.message_list
    import capo_lex_model_building_service.types.prompt_max_attempts
    import capo_lex_model_building_service.types.response_card


class Prompt(TypedDict, closed=True):
    messages: "capo_lex_model_building_service.types.message_list.MessageList"
    """<p>An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).</p>"""
    max_attempts: (
        "capo_lex_model_building_service.types.prompt_max_attempts.PromptMaxAttempts"
    )
    """<p>The number of times to prompt the user for information.</p>"""
    response_card: NotRequired[
        "capo_lex_model_building_service.types.response_card.ResponseCard"
    ]
    """<p>A response card. Amazon Lex uses this prompt at runtime, in the <code>PostText</code> API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see <a>ex-resp-card</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Prompt) -> dict:
    out: dict = {}
    import capo_lex_model_building_service.types.message_list

    out["messages"] = capo_lex_model_building_service.types.message_list.serialize_json(
        value["messages"]
    )
    out["maxAttempts"] = value["max_attempts"]
    if "response_card" in value:
        out["responseCard"] = value["response_card"]
    return out


def deserialize_json(data: dict) -> Prompt:
    out: Prompt = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import capo_lex_model_building_service.types.message_list

        out["messages"] = (
            capo_lex_model_building_service.types.message_list.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("Prompt.messages required")
    if "maxAttempts" in data:
        out["max_attempts"] = data["maxAttempts"]
    else:
        raise DeserializationError("Prompt.max_attempts required")
    if "responseCard" in data:
        out["response_card"] = data["responseCard"]
    return out
