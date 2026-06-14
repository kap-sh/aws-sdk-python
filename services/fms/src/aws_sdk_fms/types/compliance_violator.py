"""Generated from Smithy shape ``com.amazonaws.fms#ComplianceViolator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.compliance_violator_metadata
    import aws_sdk_fms.types.resource_id
    import aws_sdk_fms.types.resource_type
    import aws_sdk_fms.types.violation_reason


class ComplianceViolator(TypedDict):
    resource_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The resource ID.</p>"""
    violation_reason: NotRequired["aws_sdk_fms.types.violation_reason.ViolationReason"]
    """<p>The reason that the resource is not protected by the policy.</p>"""
    resource_type: NotRequired["aws_sdk_fms.types.resource_type.ResourceType"]
    r"""<p>The resource type. This is in the format shown in the <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html\">Amazon Web Services Resource Types Reference</a>. For example: <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code>, <code>AWS::CloudFront::Distribution</code>, or <code>AWS::NetworkFirewall::FirewallPolicy</code>.</p>"""
    metadata: NotRequired[
        "aws_sdk_fms.types.compliance_violator_metadata.ComplianceViolatorMetadata"
    ]
    """<p>Metadata about the resource that doesn't comply with the policy scope.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceViolator) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "violation_reason" in value:
        import aws_sdk_fms.types.violation_reason

        out["ViolationReason"] = (
            aws_sdk_fms.types.violation_reason.serialize_aws_json_1_1(
                value["violation_reason"]
            )
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "metadata" in value:
        import aws_sdk_fms.types.compliance_violator_metadata

        out["Metadata"] = (
            aws_sdk_fms.types.compliance_violator_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceViolator:
    out: ComplianceViolator = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ViolationReason" in data:
        import aws_sdk_fms.types.violation_reason

        out["violation_reason"] = (
            aws_sdk_fms.types.violation_reason.deserialize_aws_json_1_1(
                data["ViolationReason"]
            )
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "Metadata" in data:
        import aws_sdk_fms.types.compliance_violator_metadata

        out["metadata"] = (
            aws_sdk_fms.types.compliance_violator_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    return out
