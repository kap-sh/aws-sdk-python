"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AgentTurnResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.execution_error_details
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.test_result_slot_name
    import aws_sdk_lex_models_v2.types.test_set_agent_prompt


class AgentTurnResult(TypedDict):
    expected_agent_prompt: (
        "aws_sdk_lex_models_v2.types.test_set_agent_prompt.TestSetAgentPrompt"
    )
    """<p>The expected agent prompt for the agent turn in a test set execution.</p>"""
    actual_agent_prompt: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_agent_prompt.TestSetAgentPrompt"
    ]
    """<p>The actual agent prompt for the agent turn in a test set execution.</p>"""
    error_details: NotRequired[
        "aws_sdk_lex_models_v2.types.execution_error_details.ExecutionErrorDetails"
    ]
    actual_elicited_slot: NotRequired[
        "aws_sdk_lex_models_v2.types.test_result_slot_name.TestResultSlotName"
    ]
    """<p>The actual elicited slot for the agent turn in a test set execution.</p>"""
    actual_intent: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The actual intent for the agent turn in a test set execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentTurnResult) -> dict:
    out: dict = {}
    out["expectedAgentPrompt"] = value["expected_agent_prompt"]
    if "actual_agent_prompt" in value:
        out["actualAgentPrompt"] = value["actual_agent_prompt"]
    if "error_details" in value:
        import aws_sdk_lex_models_v2.types.execution_error_details

        out["errorDetails"] = (
            aws_sdk_lex_models_v2.types.execution_error_details.serialize_json(
                value["error_details"]
            )
        )
    if "actual_elicited_slot" in value:
        out["actualElicitedSlot"] = value["actual_elicited_slot"]
    if "actual_intent" in value:
        out["actualIntent"] = value["actual_intent"]
    return out


def deserialize_json(data: dict) -> AgentTurnResult:
    out: AgentTurnResult = {}  # type: ignore[typeddict-item]
    if "expectedAgentPrompt" in data:
        out["expected_agent_prompt"] = data["expectedAgentPrompt"]
    else:
        raise DeserializationError("AgentTurnResult.expected_agent_prompt required")
    if "actualAgentPrompt" in data:
        out["actual_agent_prompt"] = data["actualAgentPrompt"]
    if "errorDetails" in data:
        import aws_sdk_lex_models_v2.types.execution_error_details

        out["error_details"] = (
            aws_sdk_lex_models_v2.types.execution_error_details.deserialize_json(
                data["errorDetails"]
            )
        )
    if "actualElicitedSlot" in data:
        out["actual_elicited_slot"] = data["actualElicitedSlot"]
    if "actualIntent" in data:
        out["actual_intent"] = data["actualIntent"]
    return out
