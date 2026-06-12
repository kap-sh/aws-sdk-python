"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterSoftwareRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_name_or_arn
    import aws_sdk_sagemaker.types.deployment_configuration
    import aws_sdk_sagemaker.types.image_id
    import aws_sdk_sagemaker.types.update_cluster_software_instance_groups


class UpdateClusterSoftwareRequest(TypedDict):
    cluster_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>Specify the name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster you want to update for security patching.</p>"""
    instance_groups: NotRequired[
        "aws_sdk_sagemaker.types.update_cluster_software_instance_groups.UpdateClusterSoftwareInstanceGroups"
    ]
    """<p>The array of instance groups for which to update AMI versions.</p>"""
    deployment_config: NotRequired[
        "aws_sdk_sagemaker.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>The configuration to use when updating the AMI versions.</p>"""
    image_id: NotRequired["aws_sdk_sagemaker.types.image_id.ImageId"]
    """<p>When configuring your HyperPod cluster, you can specify an image ID using one of the following options:</p> <ul> <li> <p> <code>HyperPodPublicAmiId</code>: Use a HyperPod public AMI</p> </li> <li> <p> <code>CustomAmiId</code>: Use your custom AMI</p> </li> <li> <p> <code>default</code>: Use the default latest system image</p> </li> </ul> <p>If you choose to use a custom AMI (<code>CustomAmiId</code>), ensure it meets the following requirements:</p> <ul> <li> <p>Encryption: The custom AMI must be unencrypted.</p> </li> <li> <p>Ownership: The custom AMI must be owned by the same Amazon Web Services account that is creating the HyperPod cluster.</p> </li> <li> <p>Volume support: Only the primary AMI snapshot volume is supported; additional AMI volumes are not supported.</p> </li> </ul> <p>When updating the instance group's AMI through the <code>UpdateClusterSoftware</code> operation, if an instance group uses a custom AMI, you must provide an <code>ImageId</code> or use the default as input. Note that if you don't specify an instance group in your <code>UpdateClusterSoftware</code> request, then all of the instance groups are patched with the specified image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterSoftwareRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "instance_groups" in value:
        import aws_sdk_sagemaker.types.update_cluster_software_instance_groups

        out["InstanceGroups"] = (
            aws_sdk_sagemaker.types.update_cluster_software_instance_groups.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "deployment_config" in value:
        import aws_sdk_sagemaker.types.deployment_configuration

        out["DeploymentConfig"] = (
            aws_sdk_sagemaker.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterSoftwareRequest:
    out: UpdateClusterSoftwareRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "InstanceGroups" in data:
        import aws_sdk_sagemaker.types.update_cluster_software_instance_groups

        out["instance_groups"] = (
            aws_sdk_sagemaker.types.update_cluster_software_instance_groups.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if "DeploymentConfig" in data:
        import aws_sdk_sagemaker.types.deployment_configuration

        out["deployment_config"] = (
            aws_sdk_sagemaker.types.deployment_configuration.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    return out
