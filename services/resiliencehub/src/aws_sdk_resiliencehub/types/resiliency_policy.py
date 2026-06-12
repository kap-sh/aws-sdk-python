"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResiliencyPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.data_location_constraint
    import aws_sdk_resiliencehub.types.disruption_policy
    import aws_sdk_resiliencehub.types.entity_description
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.estimated_cost_tier
    import aws_sdk_resiliencehub.types.resiliency_policy_tier
    import aws_sdk_resiliencehub.types.tag_map
    import aws_sdk_resiliencehub.types.time_stamp


class ResiliencyPolicy(TypedDict):
    policy_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    policy_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>The name of the policy</p>"""
    policy_description: NotRequired[
        "aws_sdk_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Description of the resiliency policy.</p>"""
    data_location_constraint: NotRequired[
        "aws_sdk_resiliencehub.types.data_location_constraint.DataLocationConstraint"
    ]
    """<p>Specifies a high-level geographical location constraint for where your resilience policy data can be stored.</p>"""
    tier: NotRequired[
        "aws_sdk_resiliencehub.types.resiliency_policy_tier.ResiliencyPolicyTier"
    ]
    """<p>The tier for this resiliency policy, ranging from the highest severity (<code>MissionCritical</code>) to lowest (<code>NonCritical</code>).</p>"""
    estimated_cost_tier: NotRequired[
        "aws_sdk_resiliencehub.types.estimated_cost_tier.EstimatedCostTier"
    ]
    """<p>Specifies the estimated cost tier of the resiliency policy.</p>"""
    policy: NotRequired[
        "aws_sdk_resiliencehub.types.disruption_policy.DisruptionPolicy"
    ]
    """<p>The resiliency policy.</p>"""
    creation_time: NotRequired["aws_sdk_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Date and time when the resiliency policy was created.</p>"""
    tags: NotRequired["aws_sdk_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResiliencyPolicy) -> dict:
    out: dict = {}
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "policy_name" in value:
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
    if "tier" in value:
        import aws_sdk_resiliencehub.types.resiliency_policy_tier

        out["tier"] = aws_sdk_resiliencehub.types.resiliency_policy_tier.serialize_json(
            value["tier"]
        )
    if "estimated_cost_tier" in value:
        import aws_sdk_resiliencehub.types.estimated_cost_tier

        out["estimatedCostTier"] = (
            aws_sdk_resiliencehub.types.estimated_cost_tier.serialize_json(
                value["estimated_cost_tier"]
            )
        )
    if "policy" in value:
        import aws_sdk_resiliencehub.types.disruption_policy

        out["policy"] = aws_sdk_resiliencehub.types.disruption_policy.serialize_json(
            value["policy"]
        )
    if "creation_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["creationTime"] = aws_sdk_resiliencehub.types.time_stamp.serialize_json(
            value["creation_time"]
        )
    if "tags" in value:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ResiliencyPolicy:
    out: ResiliencyPolicy = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
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
    if "estimatedCostTier" in data:
        import aws_sdk_resiliencehub.types.estimated_cost_tier

        out["estimated_cost_tier"] = (
            aws_sdk_resiliencehub.types.estimated_cost_tier.deserialize_json(
                data["estimatedCostTier"]
            )
        )
    if "policy" in data:
        import aws_sdk_resiliencehub.types.disruption_policy

        out["policy"] = aws_sdk_resiliencehub.types.disruption_policy.deserialize_json(
            data["policy"]
        )
    if "creationTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["creation_time"] = aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
            data["creationTime"]
        )
    if "tags" in data:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    return out
