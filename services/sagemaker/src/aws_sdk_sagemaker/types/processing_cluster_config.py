"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingClusterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.processing_instance_count
    import aws_sdk_sagemaker.types.processing_instance_type
    import aws_sdk_sagemaker.types.processing_volume_size_in_gb


class ProcessingClusterConfig(TypedDict):
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.processing_instance_count.ProcessingInstanceCount"
    ]
    """<p>The number of ML compute instances to use in the processing job. For distributed processing jobs, specify a value greater than 1. The default value is 1.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.processing_instance_type.ProcessingInstanceType"
    ]
    """<p>The ML compute instance type for the processing job.</p>"""
    volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.processing_volume_size_in_gb.ProcessingVolumeSizeInGB"
    ]
    r"""<p>The size of the ML storage volume in gigabytes that you want to provision. You must specify sufficient ML storage for your scenario.</p> <note> <p>Certain Nitro-based instances include local storage with a fixed total size, dependent on the instance type. When using these instances for processing, Amazon SageMaker mounts the local instance storage instead of Amazon EBS gp2 storage. You can't request a <code>VolumeSizeInGB</code> greater than the total size of the local instance storage.</p> <p>For a list of instance types that support local instance storage, including the total size per instance type, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes\">Instance Store Volumes</a>.</p> </note>"""
    volume_kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    r"""<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the processing job. </p> <note> <p>Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You can't request a <code>VolumeKmsKeyId</code> when using an instance type with local storage.</p> <p>For a list of instance types that support local instance storage, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes\">Instance Store Volumes</a>.</p> <p>For more information about local instance storage encryption, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html\">SSD Instance Store Volumes</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingClusterConfig) -> dict:
    out: dict = {}
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.processing_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.processing_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingClusterConfig:
    out: ProcessingClusterConfig = {}  # type: ignore[typeddict-item]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.processing_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.processing_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "VolumeSizeInGB" in data:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    if "VolumeKmsKeyId" in data:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    return out
