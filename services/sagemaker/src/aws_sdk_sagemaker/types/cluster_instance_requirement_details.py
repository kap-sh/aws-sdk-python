"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceRequirementDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_types


class ClusterInstanceRequirementDetails(TypedDict):
    current_instance_types: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_types.ClusterInstanceTypes"
    ]
    """<p>The instance types currently in use by the instance group.</p>"""
    desired_instance_types: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_types.ClusterInstanceTypes"
    ]
    """<p>The desired instance types for the instance group, as specified in the most recent update request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceRequirementDetails) -> dict:
    out: dict = {}
    if "current_instance_types" in value:
        import aws_sdk_sagemaker.types.cluster_instance_types

        out["CurrentInstanceTypes"] = (
            aws_sdk_sagemaker.types.cluster_instance_types.serialize_aws_json_1_1(
                value["current_instance_types"]
            )
        )
    if "desired_instance_types" in value:
        import aws_sdk_sagemaker.types.cluster_instance_types

        out["DesiredInstanceTypes"] = (
            aws_sdk_sagemaker.types.cluster_instance_types.serialize_aws_json_1_1(
                value["desired_instance_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterInstanceRequirementDetails:
    out: ClusterInstanceRequirementDetails = {}  # type: ignore[typeddict-item]
    if "CurrentInstanceTypes" in data:
        import aws_sdk_sagemaker.types.cluster_instance_types

        out["current_instance_types"] = (
            aws_sdk_sagemaker.types.cluster_instance_types.deserialize_aws_json_1_1(
                data["CurrentInstanceTypes"]
            )
        )
    if "DesiredInstanceTypes" in data:
        import aws_sdk_sagemaker.types.cluster_instance_types

        out["desired_instance_types"] = (
            aws_sdk_sagemaker.types.cluster_instance_types.deserialize_aws_json_1_1(
                data["DesiredInstanceTypes"]
            )
        )
    return out
