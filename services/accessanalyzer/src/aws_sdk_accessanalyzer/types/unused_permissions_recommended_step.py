"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedPermissionsRecommendedStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.recommended_remediation_action
    import aws_sdk_accessanalyzer.types.timestamp


class UnusedPermissionsRecommendedStep(TypedDict):
    policy_updated_at: NotRequired["aws_sdk_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the existing policy for the unused permissions finding was last updated.</p>"""
    recommended_action: "aws_sdk_accessanalyzer.types.recommended_remediation_action.RecommendedRemediationAction"
    """<p>A recommendation of whether to create or detach a policy for an unused permissions finding.</p>"""
    recommended_policy: NotRequired["str"]
    """<p>If the recommended action for the unused permissions finding is to replace the existing policy, the contents of the recommended policy to replace the policy specified in the <code>existingPolicyId</code> field.</p>"""
    existing_policy_id: NotRequired["str"]
    """<p>If the recommended action for the unused permissions finding is to detach a policy, the ID of an existing policy to be detached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedPermissionsRecommendedStep) -> dict:
    out: dict = {}
    if "policy_updated_at" in value:
        import aws_sdk_accessanalyzer.types.timestamp

        out["policyUpdatedAt"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
            value["policy_updated_at"]
        )
    out["recommendedAction"] = value["recommended_action"]
    if "recommended_policy" in value:
        out["recommendedPolicy"] = value["recommended_policy"]
    if "existing_policy_id" in value:
        out["existingPolicyId"] = value["existing_policy_id"]
    return out


def deserialize_json(data: dict) -> UnusedPermissionsRecommendedStep:
    out: UnusedPermissionsRecommendedStep = {}  # type: ignore[typeddict-item]
    if "policyUpdatedAt" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["policy_updated_at"] = (
            aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
                data["policyUpdatedAt"]
            )
        )
    if "recommendedAction" in data:
        out["recommended_action"] = data["recommendedAction"]
    else:
        raise DeserializationError(
            "UnusedPermissionsRecommendedStep.recommended_action required"
        )
    if "recommendedPolicy" in data:
        out["recommended_policy"] = data["recommendedPolicy"]
    if "existingPolicyId" in data:
        out["existing_policy_id"] = data["existingPolicyId"]
    return out
