"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomOrchestration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.orchestration_executor


class CustomOrchestration(TypedDict):
    executor: NotRequired[
        "aws_sdk_bedrock_agent.types.orchestration_executor.OrchestrationExecutor"
    ]
    """<p> The structure of the executor invoking the actions in custom orchestration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomOrchestration) -> dict:
    out: dict = {}
    if "executor" in value:
        import aws_sdk_bedrock_agent.types.orchestration_executor

        out["executor"] = (
            aws_sdk_bedrock_agent.types.orchestration_executor.serialize_json(
                value["executor"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomOrchestration:
    out: CustomOrchestration = {}  # type: ignore[typeddict-item]
    if "executor" in data:
        import aws_sdk_bedrock_agent.types.orchestration_executor

        out["executor"] = (
            aws_sdk_bedrock_agent.types.orchestration_executor.deserialize_json(
                data["executor"]
            )
        )
    return out
