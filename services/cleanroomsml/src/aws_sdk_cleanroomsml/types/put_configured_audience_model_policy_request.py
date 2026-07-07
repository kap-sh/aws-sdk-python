"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PutConfiguredAudienceModelPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn
    import aws_sdk_cleanroomsml.types.hash
    import aws_sdk_cleanroomsml.types.policy_existence_condition
    import aws_sdk_cleanroomsml.types.resource_policy


class PutConfiguredAudienceModelPolicyRequest(TypedDict, closed=True):
    configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that the resource policy will govern.</p>"""
    configured_audience_model_policy: (
        "aws_sdk_cleanroomsml.types.resource_policy.ResourcePolicy"
    )
    """<p>The IAM resource policy.</p>"""
    previous_policy_hash: NotRequired["aws_sdk_cleanroomsml.types.hash.Hash"]
    """<p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>"""
    policy_existence_condition: NotRequired[
        "aws_sdk_cleanroomsml.types.policy_existence_condition.PolicyExistenceCondition"
    ]
    """<p>Use this to prevent unexpected concurrent modification of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfiguredAudienceModelPolicyRequest) -> dict:
    out: dict = {}
    out["configuredAudienceModelPolicy"] = value["configured_audience_model_policy"]
    if "previous_policy_hash" in value:
        out["previousPolicyHash"] = value["previous_policy_hash"]
    if "policy_existence_condition" in value:
        import aws_sdk_cleanroomsml.types.policy_existence_condition

        out["policyExistenceCondition"] = (
            aws_sdk_cleanroomsml.types.policy_existence_condition.serialize_json(
                value["policy_existence_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutConfiguredAudienceModelPolicyRequest:
    out: PutConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
    if "configuredAudienceModelPolicy" in data:
        out["configured_audience_model_policy"] = data["configuredAudienceModelPolicy"]
    else:
        raise DeserializationError(
            "PutConfiguredAudienceModelPolicyRequest.configured_audience_model_policy required"
        )
    if "previousPolicyHash" in data:
        out["previous_policy_hash"] = data["previousPolicyHash"]
    if "policyExistenceCondition" in data:
        import aws_sdk_cleanroomsml.types.policy_existence_condition

        out["policy_existence_condition"] = (
            aws_sdk_cleanroomsml.types.policy_existence_condition.deserialize_json(
                data["policyExistenceCondition"]
            )
        )
    return out
