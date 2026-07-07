"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyScenarios``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario_list


class AutomatedReasoningPolicyScenarios(TypedDict, closed=True):
    policy_scenarios: "aws_sdk_bedrock.types.automated_reasoning_policy_scenario_list.AutomatedReasoningPolicyScenarioList"
    """<p>Represents a collection of generated policy scenarios.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyScenarios) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario_list

    out["policyScenarios"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_scenario_list.serialize_json(
            value["policy_scenarios"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyScenarios:
    out: AutomatedReasoningPolicyScenarios = {}  # type: ignore[typeddict-item]
    if "policyScenarios" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_scenario_list

        out["policy_scenarios"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_scenario_list.deserialize_json(
                data["policyScenarios"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyScenarios.policy_scenarios required"
        )
    return out
