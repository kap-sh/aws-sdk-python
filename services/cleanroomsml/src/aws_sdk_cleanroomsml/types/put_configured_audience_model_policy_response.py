"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PutConfiguredAudienceModelPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.hash
    import aws_sdk_cleanroomsml.types.resource_policy


class PutConfiguredAudienceModelPolicyResponse(TypedDict, closed=True):
    configured_audience_model_policy: (
        "aws_sdk_cleanroomsml.types.resource_policy.ResourcePolicy"
    )
    """<p>The IAM resource policy.</p>"""
    policy_hash: "aws_sdk_cleanroomsml.types.hash.Hash"
    """<p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfiguredAudienceModelPolicyResponse) -> dict:
    out: dict = {}
    out["configuredAudienceModelPolicy"] = value["configured_audience_model_policy"]
    out["policyHash"] = value["policy_hash"]
    return out


def deserialize_json(data: dict) -> PutConfiguredAudienceModelPolicyResponse:
    out: PutConfiguredAudienceModelPolicyResponse = {}  # type: ignore[typeddict-item]
    if "configuredAudienceModelPolicy" in data:
        out["configured_audience_model_policy"] = data["configuredAudienceModelPolicy"]
    else:
        raise DeserializationError(
            "PutConfiguredAudienceModelPolicyResponse.configured_audience_model_policy required"
        )
    if "policyHash" in data:
        out["policy_hash"] = data["policyHash"]
    else:
        raise DeserializationError(
            "PutConfiguredAudienceModelPolicyResponse.policy_hash required"
        )
    return out
