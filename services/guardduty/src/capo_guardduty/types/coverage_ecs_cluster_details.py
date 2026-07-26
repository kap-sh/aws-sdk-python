"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageEcsClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.container_instance_details
    import capo_guardduty.types.fargate_details
    import capo_guardduty.types.string


class CoverageEcsClusterDetails(TypedDict, closed=True):
    cluster_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the Amazon ECS cluster.</p>"""
    fargate_details: NotRequired["capo_guardduty.types.fargate_details.FargateDetails"]
    """<p>Information about the Fargate details associated with the Amazon ECS cluster.</p>"""
    container_instance_details: NotRequired[
        "capo_guardduty.types.container_instance_details.ContainerInstanceDetails"
    ]
    """<p>Information about the Amazon ECS container running on Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageEcsClusterDetails) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "fargate_details" in value:
        import capo_guardduty.types.fargate_details

        out["fargateDetails"] = capo_guardduty.types.fargate_details.serialize_json(
            value["fargate_details"]
        )
    if "container_instance_details" in value:
        import capo_guardduty.types.container_instance_details

        out["containerInstanceDetails"] = (
            capo_guardduty.types.container_instance_details.serialize_json(
                value["container_instance_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoverageEcsClusterDetails:
    out: CoverageEcsClusterDetails = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "fargateDetails" in data:
        import capo_guardduty.types.fargate_details

        out["fargate_details"] = capo_guardduty.types.fargate_details.deserialize_json(
            data["fargateDetails"]
        )
    if "containerInstanceDetails" in data:
        import capo_guardduty.types.container_instance_details

        out["container_instance_details"] = (
            capo_guardduty.types.container_instance_details.deserialize_json(
                data["containerInstanceDetails"]
            )
        )
    return out
