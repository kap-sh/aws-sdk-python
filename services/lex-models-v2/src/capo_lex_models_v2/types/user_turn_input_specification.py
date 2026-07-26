"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UserTurnInputSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.input_session_state_specification
    import capo_lex_models_v2.types.string_map
    import capo_lex_models_v2.types.utterance_input_specification


class UserTurnInputSpecification(TypedDict, closed=True):
    utterance_input: "capo_lex_models_v2.types.utterance_input_specification.UtteranceInputSpecification"
    """<p>The utterance input in the user turn.</p>"""
    request_attributes: NotRequired["capo_lex_models_v2.types.string_map.StringMap"]
    """<p>Request attributes of the user turn.</p>"""
    session_state: NotRequired[
        "capo_lex_models_v2.types.input_session_state_specification.InputSessionStateSpecification"
    ]
    """<p>Contains information about the session state in the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserTurnInputSpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.utterance_input_specification

    out["utteranceInput"] = (
        capo_lex_models_v2.types.utterance_input_specification.serialize_json(
            value["utterance_input"]
        )
    )
    if "request_attributes" in value:
        import capo_lex_models_v2.types.string_map

        out["requestAttributes"] = capo_lex_models_v2.types.string_map.serialize_json(
            value["request_attributes"]
        )
    if "session_state" in value:
        import capo_lex_models_v2.types.input_session_state_specification

        out["sessionState"] = (
            capo_lex_models_v2.types.input_session_state_specification.serialize_json(
                value["session_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserTurnInputSpecification:
    out: UserTurnInputSpecification = {}  # type: ignore[typeddict-item]
    if "utteranceInput" in data:
        import capo_lex_models_v2.types.utterance_input_specification

        out["utterance_input"] = (
            capo_lex_models_v2.types.utterance_input_specification.deserialize_json(
                data["utteranceInput"]
            )
        )
    else:
        raise DeserializationError(
            "UserTurnInputSpecification.utterance_input required"
        )
    if "requestAttributes" in data:
        import capo_lex_models_v2.types.string_map

        out["request_attributes"] = (
            capo_lex_models_v2.types.string_map.deserialize_json(
                data["requestAttributes"]
            )
        )
    if "sessionState" in data:
        import capo_lex_models_v2.types.input_session_state_specification

        out["session_state"] = (
            capo_lex_models_v2.types.input_session_state_specification.deserialize_json(
                data["sessionState"]
            )
        )
    return out
