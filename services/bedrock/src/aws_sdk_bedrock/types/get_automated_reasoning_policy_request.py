"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn


class GetAutomatedReasoningPolicyRequest(TypedDict, closed=True):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to retrieve. Can be either the unversioned ARN for the draft policy or an ARN for a specific policy version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyRequest:
    out: GetAutomatedReasoningPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
