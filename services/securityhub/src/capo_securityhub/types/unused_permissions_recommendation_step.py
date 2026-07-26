"""Generated from Smithy shape ``com.amazonaws.securityhub#UnusedPermissionsRecommendationStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.timestamp


class UnusedPermissionsRecommendationStep(TypedDict, closed=True):
    recommended_action: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A recommendation of whether to create or detach a policy for an unused permissions finding.</p>"""
    existing_policy: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The contents of the existing policy identified by <code>ExistingPolicyId</code> which needs to be replaced, when the <code>RecommendedAction</code> is <code>CREATE_POLICY</code>.</p>"""
    existing_policy_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of an existing policy to be replaced or detached.</p>"""
    policy_updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The time at which the existing policy for the unused permissions finding was last updated.</p>"""
    recommended_policy: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The contents of the least-privileged recommended replacement for <code>ExistingPolicyId</code>, when the <code>RecommendedAction</code> is <code>CREATE_POLICY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedPermissionsRecommendationStep) -> dict:
    out: dict = {}
    if "recommended_action" in value:
        out["RecommendedAction"] = value["recommended_action"]
    if "existing_policy" in value:
        out["ExistingPolicy"] = value["existing_policy"]
    if "existing_policy_id" in value:
        out["ExistingPolicyId"] = value["existing_policy_id"]
    if "policy_updated_at" in value:
        import capo_securityhub.types.timestamp

        out["PolicyUpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["policy_updated_at"]
        )
    if "recommended_policy" in value:
        out["RecommendedPolicy"] = value["recommended_policy"]
    return out


def deserialize_json(data: dict) -> UnusedPermissionsRecommendationStep:
    out: UnusedPermissionsRecommendationStep = {}  # type: ignore[typeddict-item]
    if "RecommendedAction" in data:
        out["recommended_action"] = data["RecommendedAction"]
    if "ExistingPolicy" in data:
        out["existing_policy"] = data["ExistingPolicy"]
    if "ExistingPolicyId" in data:
        out["existing_policy_id"] = data["ExistingPolicyId"]
    if "PolicyUpdatedAt" in data:
        import capo_securityhub.types.timestamp

        out["policy_updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["PolicyUpdatedAt"]
        )
    if "RecommendedPolicy" in data:
        out["recommended_policy"] = data["RecommendedPolicy"]
    return out
