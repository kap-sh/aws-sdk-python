"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CustomOrchestration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.orchestration_executor


class CustomOrchestration(TypedDict, closed=True):
    executor: NotRequired[
        "capo_bedrock_agent_runtime.types.orchestration_executor.OrchestrationExecutor"
    ]
    """<p>The structure of the executor invoking the actions in custom orchestration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomOrchestration) -> dict:
    out: dict = {}
    if "executor" in value:
        import capo_bedrock_agent_runtime.types.orchestration_executor

        out["executor"] = (
            capo_bedrock_agent_runtime.types.orchestration_executor.serialize_json(
                value["executor"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomOrchestration:
    out: CustomOrchestration = {}  # type: ignore[typeddict-item]
    if data.get("executor") is not None:
        import capo_bedrock_agent_runtime.types.orchestration_executor

        out["executor"] = (
            capo_bedrock_agent_runtime.types.orchestration_executor.deserialize_json(
                data["executor"]
            )
        )
    return out
