"""Generated from Smithy shape ``com.amazonaws.sagemaker#AcceleratorPartitionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.mig_profile_type


class AcceleratorPartitionConfig(TypedDict, closed=True):
    type: NotRequired["aws_sdk_sagemaker.types.mig_profile_type.MIGProfileType"]
    """<p>The Multi-Instance GPU (MIG) profile type that defines the partition configuration. The profile specifies the compute and memory allocation for each partition instance. The available profile types depend on the instance type specified in the compute quota configuration.</p>"""
    count: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The number of accelerator partitions to allocate with the specified partition type. If you don't specify a value for vCPU and MemoryInGiB, SageMaker AI automatically allocates ratio-based values for those parameters based on the accelerator partition count you provide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorPartitionConfig) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_sagemaker.types.mig_profile_type

        out["Type"] = aws_sdk_sagemaker.types.mig_profile_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceleratorPartitionConfig:
    out: AcceleratorPartitionConfig = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_sagemaker.types.mig_profile_type

        out["type"] = aws_sdk_sagemaker.types.mig_profile_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Count" in data:
        out["count"] = data["Count"]
    return out
