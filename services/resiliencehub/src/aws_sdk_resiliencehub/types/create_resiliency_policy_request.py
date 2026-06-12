"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateResiliencyPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.client_token
    import aws_sdk_resiliencehub.types.data_location_constraint
    import aws_sdk_resiliencehub.types.disruption_policy
    import aws_sdk_resiliencehub.types.entity_description
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.resiliency_policy_tier
    import aws_sdk_resiliencehub.types.tag_map


class CreateResiliencyPolicyRequest(TypedDict):
    policy_name: "aws_sdk_resiliencehub.types.entity_name.EntityName"
    """<p>Name of the resiliency policy.</p>"""
    policy_description: NotRequired[
        "aws_sdk_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Description of the resiliency policy.</p>"""
    data_location_constraint: NotRequired[
        "aws_sdk_resiliencehub.types.data_location_constraint.DataLocationConstraint"
    ]
    """<p>Specifies a high-level geographical location constraint for where your resilience policy data can be stored.</p>"""
    tier: "aws_sdk_resiliencehub.types.resiliency_policy_tier.ResiliencyPolicyTier"
    """<p>The tier for this resiliency policy, ranging from the highest severity (<code>MissionCritical</code>) to lowest (<code>NonCritical</code>).</p>"""
    policy: "aws_sdk_resiliencehub.types.disruption_policy.DisruptionPolicy"
    """<p>The type of resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.</p>"""
    client_token: NotRequired["aws_sdk_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""
    tags: NotRequired["aws_sdk_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResiliencyPolicyRequest) -> dict:
    out: dict = {}
    out["policyName"] = value["policy_name"]
    if "policy_description" in value:
        out["policyDescription"] = value["policy_description"]
    if "data_location_constraint" in value:
        import aws_sdk_resiliencehub.types.data_location_constraint

        out["dataLocationConstraint"] = (
            aws_sdk_resiliencehub.types.data_location_constraint.serialize_json(
                value["data_location_constraint"]
            )
        )
    import aws_sdk_resiliencehub.types.resiliency_policy_tier

    out["tier"] = aws_sdk_resiliencehub.types.resiliency_policy_tier.serialize_json(
        value["tier"]
    )
    import aws_sdk_resiliencehub.types.disruption_policy

    out["policy"] = aws_sdk_resiliencehub.types.disruption_policy.serialize_json(
        value["policy"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateResiliencyPolicyRequest:
    out: CreateResiliencyPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    else:
        raise DeserializationError("CreateResiliencyPolicyRequest.policy_name required")
    if "policyDescription" in data:
        out["policy_description"] = data["policyDescription"]
    if "dataLocationConstraint" in data:
        import aws_sdk_resiliencehub.types.data_location_constraint

        out["data_location_constraint"] = (
            aws_sdk_resiliencehub.types.data_location_constraint.deserialize_json(
                data["dataLocationConstraint"]
            )
        )
    if "tier" in data:
        import aws_sdk_resiliencehub.types.resiliency_policy_tier

        out["tier"] = (
            aws_sdk_resiliencehub.types.resiliency_policy_tier.deserialize_json(
                data["tier"]
            )
        )
    else:
        raise DeserializationError("CreateResiliencyPolicyRequest.tier required")
    if "policy" in data:
        import aws_sdk_resiliencehub.types.disruption_policy

        out["policy"] = aws_sdk_resiliencehub.types.disruption_policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("CreateResiliencyPolicyRequest.policy required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    return out
