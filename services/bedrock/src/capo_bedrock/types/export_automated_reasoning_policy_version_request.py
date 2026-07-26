"""Generated from Smithy shape ``com.amazonaws.bedrock#ExportAutomatedReasoningPolicyVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn


class ExportAutomatedReasoningPolicyVersionRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to export. Can be either the unversioned ARN for the draft policy or a versioned ARN for a specific policy version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAutomatedReasoningPolicyVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExportAutomatedReasoningPolicyVersionRequest:
    out: ExportAutomatedReasoningPolicyVersionRequest = {}  # type: ignore[typeddict-item]
    return out
