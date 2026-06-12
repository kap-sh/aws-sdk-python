"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyNextScenarioResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_scenario


class GetAutomatedReasoningPolicyNextScenarioResponse(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>"""
    scenario: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_scenario.AutomatedReasoningPolicyScenario"
    ]
    """<p>The next test scenario to validate, including the test expression and expected results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyNextScenarioResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    if "scenario" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_scenario

        out["scenario"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_scenario.serialize_json(
                value["scenario"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyNextScenarioResponse:
    out: GetAutomatedReasoningPolicyNextScenarioResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyNextScenarioResponse.policy_arn required"
        )
    if "scenario" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_scenario

        out["scenario"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_scenario.deserialize_json(
                data["scenario"]
            )
        )
    return out
