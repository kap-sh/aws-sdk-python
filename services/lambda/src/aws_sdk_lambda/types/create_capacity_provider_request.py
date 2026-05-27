"""Generated from Smithy shape ``com.amazonaws.lambda#CreateCapacityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_name
    import aws_sdk_lambda.types.capacity_provider_permissions_config
    import aws_sdk_lambda.types.capacity_provider_scaling_config
    import aws_sdk_lambda.types.capacity_provider_vpc_config
    import aws_sdk_lambda.types.instance_requirements
    import aws_sdk_lambda.types.kms_key_arn_non_empty
    import aws_sdk_lambda.types.tags


class CreateCapacityProviderRequest(TypedDict):
    capacity_provider_name: (
        "aws_sdk_lambda.types.capacity_provider_name.CapacityProviderName"
    )
    """<p>The name of the capacity provider. </p>"""
    vpc_config: (
        "aws_sdk_lambda.types.capacity_provider_vpc_config.CapacityProviderVpcConfig"
    )
    """<p>The VPC configuration for the capacity provider, including subnet IDs and security group IDs where compute instances will be launched.</p>"""
    permissions_config: "aws_sdk_lambda.types.capacity_provider_permissions_config.CapacityProviderPermissionsConfig"
    """<p>The permissions configuration that specifies the IAM role ARN used by the capacity provider to manage compute resources.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_lambda.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The instance requirements that specify the compute instance characteristics, including architectures and allowed or excluded instance types.</p>"""
    capacity_provider_scaling_config: NotRequired[
        "aws_sdk_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
    ]
    """<p>The scaling configuration that defines how the capacity provider scales compute instances, including maximum vCPU count and scaling policies.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_lambda.types.kms_key_arn_non_empty.KMSKeyArnNonEmpty"
    ]
    """<p>The ARN of the KMS key used to encrypt data associated with the capacity provider.</p>"""
    tags: NotRequired["aws_sdk_lambda.types.tags.Tags"]
    """<p>A list of tags to associate with the capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCapacityProviderRequest) -> dict:
    out: dict = {}
    out["CapacityProviderName"] = value["capacity_provider_name"]
    import aws_sdk_lambda.types.capacity_provider_vpc_config

    out["VpcConfig"] = aws_sdk_lambda.types.capacity_provider_vpc_config.serialize_json(
        value["vpc_config"]
    )
    import aws_sdk_lambda.types.capacity_provider_permissions_config

    out["PermissionsConfig"] = (
        aws_sdk_lambda.types.capacity_provider_permissions_config.serialize_json(
            value["permissions_config"]
        )
    )
    if "instance_requirements" in value:
        import aws_sdk_lambda.types.instance_requirements

        out["InstanceRequirements"] = (
            aws_sdk_lambda.types.instance_requirements.serialize_json(
                value["instance_requirements"]
            )
        )
    if "capacity_provider_scaling_config" in value:
        import aws_sdk_lambda.types.capacity_provider_scaling_config

        out["CapacityProviderScalingConfig"] = (
            aws_sdk_lambda.types.capacity_provider_scaling_config.serialize_json(
                value["capacity_provider_scaling_config"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_lambda.types.tags

        out["Tags"] = aws_sdk_lambda.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCapacityProviderRequest:
    out: CreateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    if "CapacityProviderName" in data:
        out["capacity_provider_name"] = data["CapacityProviderName"]
    else:
        raise DeserializationError(
            "CreateCapacityProviderRequest.capacity_provider_name required"
        )
    if "VpcConfig" in data:
        import aws_sdk_lambda.types.capacity_provider_vpc_config

        out["vpc_config"] = (
            aws_sdk_lambda.types.capacity_provider_vpc_config.deserialize_json(
                data["VpcConfig"]
            )
        )
    else:
        raise DeserializationError("CreateCapacityProviderRequest.vpc_config required")
    if "PermissionsConfig" in data:
        import aws_sdk_lambda.types.capacity_provider_permissions_config

        out["permissions_config"] = (
            aws_sdk_lambda.types.capacity_provider_permissions_config.deserialize_json(
                data["PermissionsConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCapacityProviderRequest.permissions_config required"
        )
    if "InstanceRequirements" in data:
        import aws_sdk_lambda.types.instance_requirements

        out["instance_requirements"] = (
            aws_sdk_lambda.types.instance_requirements.deserialize_json(
                data["InstanceRequirements"]
            )
        )
    if "CapacityProviderScalingConfig" in data:
        import aws_sdk_lambda.types.capacity_provider_scaling_config

        out["capacity_provider_scaling_config"] = (
            aws_sdk_lambda.types.capacity_provider_scaling_config.deserialize_json(
                data["CapacityProviderScalingConfig"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "Tags" in data:
        import aws_sdk_lambda.types.tags

        out["tags"] = aws_sdk_lambda.types.tags.deserialize_json(data["Tags"])
    return out
