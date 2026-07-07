"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringClusterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.processing_instance_count
    import aws_sdk_sagemaker.types.processing_instance_type
    import aws_sdk_sagemaker.types.processing_volume_size_in_gb


class MonitoringClusterConfig(TypedDict, closed=True):
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.processing_instance_count.ProcessingInstanceCount"
    ]
    """<p>The number of ML compute instances to use in the model monitoring job. For distributed processing jobs, specify a value greater than 1. The default value is 1.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.processing_instance_type.ProcessingInstanceType"
    ]
    """<p>The ML compute instance type for the processing job.</p>"""
    volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.processing_volume_size_in_gb.ProcessingVolumeSizeInGB"
    ]
    """<p>The size of the ML storage volume, in gigabytes, that you want to provision. You must specify sufficient ML storage for your scenario.</p>"""
    volume_kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Key Management Service (KMS) key that Amazon SageMaker AI uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the model monitoring job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringClusterConfig) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> MonitoringClusterConfig:
    out: MonitoringClusterConfig = {}  # type: ignore[typeddict-item]
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
