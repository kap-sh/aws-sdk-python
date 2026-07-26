"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetConfiguredAudienceModelPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.hash
    import capo_cleanroomsml.types.resource_policy


class GetConfiguredAudienceModelPolicyResponse(TypedDict, closed=True):
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model.</p>"""
    configured_audience_model_policy: (
        "capo_cleanroomsml.types.resource_policy.ResourcePolicy"
    )
    """<p>The configured audience model policy. This is a JSON IAM resource policy.</p>"""
    policy_hash: "capo_cleanroomsml.types.hash.Hash"
    """<p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredAudienceModelPolicyResponse) -> dict:
    out: dict = {}
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    out["configuredAudienceModelPolicy"] = value["configured_audience_model_policy"]
    out["policyHash"] = value["policy_hash"]
    return out


def deserialize_json(data: dict) -> GetConfiguredAudienceModelPolicyResponse:
    out: GetConfiguredAudienceModelPolicyResponse = {}  # type: ignore[typeddict-item]
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelPolicyResponse.configured_audience_model_arn required"
        )
    if "configuredAudienceModelPolicy" in data:
        out["configured_audience_model_policy"] = data["configuredAudienceModelPolicy"]
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelPolicyResponse.configured_audience_model_policy required"
        )
    if "policyHash" in data:
        out["policy_hash"] = data["policyHash"]
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelPolicyResponse.policy_hash required"
        )
    return out
