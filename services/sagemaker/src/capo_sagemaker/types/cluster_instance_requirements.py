"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_instance_types


class ClusterInstanceRequirements(TypedDict, closed=True):
    instance_types: NotRequired[
        "capo_sagemaker.types.cluster_instance_types.ClusterInstanceTypes"
    ]
    """<p>The list of instance types that the instance group can use. The order of instance types determines the priority—HyperPod attempts to provision instances using the first instance type in the list and falls back to subsequent types if capacity is unavailable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceRequirements) -> dict:
    out: dict = {}
    if "instance_types" in value:
        import capo_sagemaker.types.cluster_instance_types

        out["InstanceTypes"] = (
            capo_sagemaker.types.cluster_instance_types.serialize_aws_json_1_1(
                value["instance_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterInstanceRequirements:
    out: ClusterInstanceRequirements = {}  # type: ignore[typeddict-item]
    if "InstanceTypes" in data:
        import capo_sagemaker.types.cluster_instance_types

        out["instance_types"] = (
            capo_sagemaker.types.cluster_instance_types.deserialize_aws_json_1_1(
                data["InstanceTypes"]
            )
        )
    return out
