"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterEbsVolumeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.cluster_ebs_volume_size_in_gb
    import capo_sagemaker.types.kms_key_id


class ClusterEbsVolumeConfig(TypedDict, closed=True):
    volume_size_in_gb: NotRequired[
        "capo_sagemaker.types.cluster_ebs_volume_size_in_gb.ClusterEbsVolumeSizeInGB"
    ]
    """<p>The size in gigabytes (GB) of the additional EBS volume to be attached to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to <code>/opt/sagemaker</code>.</p>"""
    volume_kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The ID of a KMS key to encrypt the Amazon EBS volume.</p>"""
    root_volume: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Specifies whether the configuration is for the cluster's root or secondary Amazon EBS volume. You can specify two <code>ClusterEbsVolumeConfig</code> fields to configure both the root and secondary volumes. Set the value to <code>True</code> if you'd like to provide your own customer managed Amazon Web Services KMS key to encrypt the root volume. When <code>True</code>:</p> <ul> <li> <p>The configuration is applied to the root volume.</p> </li> <li> <p>You can't specify the <code>VolumeSizeInGB</code> field. The size of the root volume is determined for you.</p> </li> <li> <p>You must specify a KMS key ID for <code>VolumeKmsKeyId</code> to encrypt the root volume with your own KMS key instead of an Amazon Web Services owned KMS key.</p> </li> </ul> <p>Otherwise, by default, the value is <code>False</code>, and the following applies:</p> <ul> <li> <p>The configuration is applied to the secondary volume, while the root volume is encrypted with an Amazon Web Services owned key.</p> </li> <li> <p>You must specify the <code>VolumeSizeInGB</code> field.</p> </li> <li> <p>You can optionally specify the <code>VolumeKmsKeyId</code> to encrypt the secondary volume with your own KMS key instead of an Amazon Web Services owned KMS key.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterEbsVolumeConfig) -> dict:
    out: dict = {}
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "root_volume" in value:
        out["RootVolume"] = value["root_volume"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterEbsVolumeConfig:
    out: ClusterEbsVolumeConfig = {}  # type: ignore[typeddict-item]
    if "VolumeSizeInGB" in data:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    if "VolumeKmsKeyId" in data:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if "RootVolume" in data:
        out["root_volume"] = data["RootVolume"]
    return out
