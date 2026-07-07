"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetTurnResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.agent_turn_result
    import aws_sdk_lex_models_v2.types.user_turn_result


class TestSetTurnResult(TypedDict, closed=True):
    agent: NotRequired["aws_sdk_lex_models_v2.types.agent_turn_result.AgentTurnResult"]
    """<p>Contains information about the agent messages in the turn.</p>"""
    user: NotRequired["aws_sdk_lex_models_v2.types.user_turn_result.UserTurnResult"]
    """<p>Contains information about the user messages in the turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetTurnResult) -> dict:
    out: dict = {}
    if "agent" in value:
        import aws_sdk_lex_models_v2.types.agent_turn_result

        out["agent"] = aws_sdk_lex_models_v2.types.agent_turn_result.serialize_json(
            value["agent"]
        )
    if "user" in value:
        import aws_sdk_lex_models_v2.types.user_turn_result

        out["user"] = aws_sdk_lex_models_v2.types.user_turn_result.serialize_json(
            value["user"]
        )
    return out


def deserialize_json(data: dict) -> TestSetTurnResult:
    out: TestSetTurnResult = {}  # type: ignore[typeddict-item]
    if "agent" in data:
        import aws_sdk_lex_models_v2.types.agent_turn_result

        out["agent"] = aws_sdk_lex_models_v2.types.agent_turn_result.deserialize_json(
            data["agent"]
        )
    if "user" in data:
        import aws_sdk_lex_models_v2.types.user_turn_result

        out["user"] = aws_sdk_lex_models_v2.types.user_turn_result.deserialize_json(
            data["user"]
        )
    return out
