"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TurnSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.agent_turn_specification
    import aws_sdk_lex_models_v2.types.user_turn_specification


class TurnSpecification(TypedDict, closed=True):
    agent_turn: NotRequired[
        "aws_sdk_lex_models_v2.types.agent_turn_specification.AgentTurnSpecification"
    ]
    """<p>Contains information about the agent messages in the turn.</p>"""
    user_turn: NotRequired[
        "aws_sdk_lex_models_v2.types.user_turn_specification.UserTurnSpecification"
    ]
    """<p>Contains information about the user messages in the turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TurnSpecification) -> dict:
    out: dict = {}
    if "agent_turn" in value:
        import aws_sdk_lex_models_v2.types.agent_turn_specification

        out["agentTurn"] = (
            aws_sdk_lex_models_v2.types.agent_turn_specification.serialize_json(
                value["agent_turn"]
            )
        )
    if "user_turn" in value:
        import aws_sdk_lex_models_v2.types.user_turn_specification

        out["userTurn"] = (
            aws_sdk_lex_models_v2.types.user_turn_specification.serialize_json(
                value["user_turn"]
            )
        )
    return out


def deserialize_json(data: dict) -> TurnSpecification:
    out: TurnSpecification = {}  # type: ignore[typeddict-item]
    if "agentTurn" in data:
        import aws_sdk_lex_models_v2.types.agent_turn_specification

        out["agent_turn"] = (
            aws_sdk_lex_models_v2.types.agent_turn_specification.deserialize_json(
                data["agentTurn"]
            )
        )
    if "userTurn" in data:
        import aws_sdk_lex_models_v2.types.user_turn_specification

        out["user_turn"] = (
            aws_sdk_lex_models_v2.types.user_turn_specification.deserialize_json(
                data["userTurn"]
            )
        )
    return out
