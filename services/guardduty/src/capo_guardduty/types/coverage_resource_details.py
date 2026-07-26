"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.coverage_ec2_instance_details
    import capo_guardduty.types.coverage_ecs_cluster_details
    import capo_guardduty.types.coverage_eks_cluster_details
    import capo_guardduty.types.resource_type


class CoverageResourceDetails(TypedDict, closed=True):
    eks_cluster_details: NotRequired[
        "capo_guardduty.types.coverage_eks_cluster_details.CoverageEksClusterDetails"
    ]
    """<p>EKS cluster details involved in the coverage statistics.</p>"""
    ecs_cluster_details: NotRequired[
        "capo_guardduty.types.coverage_ecs_cluster_details.CoverageEcsClusterDetails"
    ]
    """<p>Information about the Amazon ECS cluster that is assessed for runtime coverage.</p>"""
    ec2_instance_details: NotRequired[
        "capo_guardduty.types.coverage_ec2_instance_details.CoverageEc2InstanceDetails"
    ]
    """<p>Information about the Amazon EC2 instance assessed for runtime coverage.</p>"""
    resource_type: NotRequired["capo_guardduty.types.resource_type.ResourceType"]
    """<p>The type of Amazon Web Services resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageResourceDetails) -> dict:
    out: dict = {}
    if "eks_cluster_details" in value:
        import capo_guardduty.types.coverage_eks_cluster_details

        out["eksClusterDetails"] = (
            capo_guardduty.types.coverage_eks_cluster_details.serialize_json(
                value["eks_cluster_details"]
            )
        )
    if "ecs_cluster_details" in value:
        import capo_guardduty.types.coverage_ecs_cluster_details

        out["ecsClusterDetails"] = (
            capo_guardduty.types.coverage_ecs_cluster_details.serialize_json(
                value["ecs_cluster_details"]
            )
        )
    if "ec2_instance_details" in value:
        import capo_guardduty.types.coverage_ec2_instance_details

        out["ec2InstanceDetails"] = (
            capo_guardduty.types.coverage_ec2_instance_details.serialize_json(
                value["ec2_instance_details"]
            )
        )
    if "resource_type" in value:
        import capo_guardduty.types.resource_type

        out["resourceType"] = capo_guardduty.types.resource_type.serialize_json(
            value["resource_type"]
        )
    return out


def deserialize_json(data: dict) -> CoverageResourceDetails:
    out: CoverageResourceDetails = {}  # type: ignore[typeddict-item]
    if "eksClusterDetails" in data:
        import capo_guardduty.types.coverage_eks_cluster_details

        out["eks_cluster_details"] = (
            capo_guardduty.types.coverage_eks_cluster_details.deserialize_json(
                data["eksClusterDetails"]
            )
        )
    if "ecsClusterDetails" in data:
        import capo_guardduty.types.coverage_ecs_cluster_details

        out["ecs_cluster_details"] = (
            capo_guardduty.types.coverage_ecs_cluster_details.deserialize_json(
                data["ecsClusterDetails"]
            )
        )
    if "ec2InstanceDetails" in data:
        import capo_guardduty.types.coverage_ec2_instance_details

        out["ec2_instance_details"] = (
            capo_guardduty.types.coverage_ec2_instance_details.deserialize_json(
                data["ec2InstanceDetails"]
            )
        )
    if "resourceType" in data:
        import capo_guardduty.types.resource_type

        out["resource_type"] = capo_guardduty.types.resource_type.deserialize_json(
            data["resourceType"]
        )
    return out
