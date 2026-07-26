"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnOutputSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.active_context_list
    import capo_lex_models_v2.types.test_set_utterance_text
    import capo_lex_models_v2.types.user_turn_intent_output


class UserTurnOutputSpecification(TypedDict, closed=True):
    intent: "capo_lex_models_v2.types.user_turn_intent_output.UserTurnIntentOutput"
    """<p>Contains information about the intent.</p>"""
    active_contexts: NotRequired[
        "capo_lex_models_v2.types.active_context_list.ActiveContextList"
    ]
    """<p>The contexts that are active in the turn.</p>"""
    transcript: NotRequired[
        "capo_lex_models_v2.types.test_set_utterance_text.TestSetUtteranceText"
    ]
    """<p>The transcript that is output for the user turn by the test execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserTurnOutputSpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.user_turn_intent_output

    out["intent"] = capo_lex_models_v2.types.user_turn_intent_output.serialize_json(
        value["intent"]
    )
    if "active_contexts" in value:
        import capo_lex_models_v2.types.active_context_list

        out["activeContexts"] = (
            capo_lex_models_v2.types.active_context_list.serialize_json(
                value["active_contexts"]
            )
        )
    if "transcript" in value:
        out["transcript"] = value["transcript"]
    return out


def deserialize_json(data: dict) -> UserTurnOutputSpecification:
    out: UserTurnOutputSpecification = {}  # type: ignore[typeddict-item]
    if "intent" in data:
        import capo_lex_models_v2.types.user_turn_intent_output

        out["intent"] = (
            capo_lex_models_v2.types.user_turn_intent_output.deserialize_json(
                data["intent"]
            )
        )
    else:
        raise DeserializationError("UserTurnOutputSpecification.intent required")
    if "activeContexts" in data:
        import capo_lex_models_v2.types.active_context_list

        out["active_contexts"] = (
            capo_lex_models_v2.types.active_context_list.deserialize_json(
                data["activeContexts"]
            )
        )
    if "transcript" in data:
        out["transcript"] = data["transcript"]
    return out
