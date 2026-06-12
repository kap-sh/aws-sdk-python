"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstancePlacement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_availability_zone
    import aws_sdk_sagemaker.types.cluster_availability_zone_id


class ClusterInstancePlacement(TypedDict):
    availability_zone: NotRequired[
        "aws_sdk_sagemaker.types.cluster_availability_zone.ClusterAvailabilityZone"
    ]
    """<p>The Availability Zone where the node in the SageMaker HyperPod cluster is launched.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_sagemaker.types.cluster_availability_zone_id.ClusterAvailabilityZoneId"
    ]
    """<p>The unique identifier (ID) of the Availability Zone where the node in the SageMaker HyperPod cluster is launched.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstancePlacement) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterInstancePlacement:
    out: ClusterInstancePlacement = {}  # type: ignore[typeddict-item]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "AvailabilityZoneId" in data:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    return out
