"""Generated from Smithy shape ``com.amazonaws.bedrock#ExportAutomatedReasoningPolicyVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition


class ExportAutomatedReasoningPolicyVersionResponse(TypedDict):
    policy_definition: "aws_sdk_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
    """<p>The exported policy definition containing the formal logic rules, variables, and custom variable types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAutomatedReasoningPolicyVersionResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition

    out["policyDefinition"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition.serialize_json(
            value["policy_definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExportAutomatedReasoningPolicyVersionResponse:
    out: ExportAutomatedReasoningPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if "policyDefinition" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "ExportAutomatedReasoningPolicyVersionResponse.policy_definition required"
        )
    return out
