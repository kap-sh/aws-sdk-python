"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateAutomatedReasoningPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition
    import aws_sdk_bedrock.types.automated_reasoning_policy_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_name


class UpdateAutomatedReasoningPolicyRequest(TypedDict, closed=True):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to update. This must be the ARN of a draft policy.</p>"""
    policy_definition: "aws_sdk_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
    """<p>The updated policy definition containing the formal logic rules, variables, and types.</p>"""
    name: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    ]
    """<p>The updated name for the Automated Reasoning policy.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
    ]
    """<p>The updated description for the Automated Reasoning policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedReasoningPolicyRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition

    out["policyDefinition"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_definition.serialize_json(
            value["policy_definition"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAutomatedReasoningPolicyRequest:
    out: UpdateAutomatedReasoningPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyDefinition" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyRequest.policy_definition required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    return out
