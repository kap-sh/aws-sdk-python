"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateResiliencyPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.data_location_constraint
    import aws_sdk_resiliencehub.types.disruption_policy
    import aws_sdk_resiliencehub.types.entity_description
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.resiliency_policy_tier


class UpdateResiliencyPolicyRequest(TypedDict, closed=True):
    policy_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    policy_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the resiliency policy.</p>"""
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
    policy: NotRequired[
        "aws_sdk_resiliencehub.types.disruption_policy.DisruptionPolicy"
    ]
    """<p>Resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResiliencyPolicyRequest) -> dict:
    out: dict = {}
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
    if "policy" in value:
        import aws_sdk_resiliencehub.types.disruption_policy

        out["policy"] = aws_sdk_resiliencehub.types.disruption_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> UpdateResiliencyPolicyRequest:
    out: UpdateResiliencyPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("UpdateResiliencyPolicyRequest.policy_arn required")
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
    if "policy" in data:
        import aws_sdk_resiliencehub.types.disruption_policy

        out["policy"] = aws_sdk_resiliencehub.types.disruption_policy.deserialize_json(
            data["policy"]
        )
    return out
