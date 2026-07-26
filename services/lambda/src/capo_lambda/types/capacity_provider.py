"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_arn
    import capo_lambda.types.capacity_provider_permissions_config
    import capo_lambda.types.capacity_provider_scaling_config
    import capo_lambda.types.capacity_provider_state
    import capo_lambda.types.capacity_provider_vpc_config
    import capo_lambda.types.instance_requirements
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.timestamp


class CapacityProvider(TypedDict, closed=True):
    capacity_provider_arn: "capo_lambda.types.capacity_provider_arn.CapacityProviderArn"
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    state: "capo_lambda.types.capacity_provider_state.CapacityProviderState"
    """<p>The current state of the capacity provider.</p>"""
    vpc_config: (
        "capo_lambda.types.capacity_provider_vpc_config.CapacityProviderVpcConfig"
    )
    """<p>The VPC configuration for the capacity provider.</p>"""
    permissions_config: "capo_lambda.types.capacity_provider_permissions_config.CapacityProviderPermissionsConfig"
    """<p>The permissions configuration for the capacity provider.</p>"""
    instance_requirements: NotRequired[
        "capo_lambda.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The instance requirements for compute resources managed by the capacity provider.</p>"""
    capacity_provider_scaling_config: NotRequired[
        "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
    ]
    """<p>The scaling configuration for the capacity provider.</p>"""
    kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the KMS key used to encrypt the capacity provider's resources.</p>"""
    last_modified: NotRequired["capo_lambda.types.timestamp.Timestamp"]
    """<p>The date and time when the capacity provider was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProvider) -> dict:
    out: dict = {}
    out["CapacityProviderArn"] = value["capacity_provider_arn"]
    import capo_lambda.types.capacity_provider_state

    out["State"] = capo_lambda.types.capacity_provider_state.serialize_json(
        value["state"]
    )
    import capo_lambda.types.capacity_provider_vpc_config

    out["VpcConfig"] = capo_lambda.types.capacity_provider_vpc_config.serialize_json(
        value["vpc_config"]
    )
    import capo_lambda.types.capacity_provider_permissions_config

    out["PermissionsConfig"] = (
        capo_lambda.types.capacity_provider_permissions_config.serialize_json(
            value["permissions_config"]
        )
    )
    if "instance_requirements" in value:
        import capo_lambda.types.instance_requirements

        out["InstanceRequirements"] = (
            capo_lambda.types.instance_requirements.serialize_json(
                value["instance_requirements"]
            )
        )
    if "capacity_provider_scaling_config" in value:
        import capo_lambda.types.capacity_provider_scaling_config

        out["CapacityProviderScalingConfig"] = (
            capo_lambda.types.capacity_provider_scaling_config.serialize_json(
                value["capacity_provider_scaling_config"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> CapacityProvider:
    out: CapacityProvider = {}  # type: ignore[typeddict-item]
    if "CapacityProviderArn" in data:
        out["capacity_provider_arn"] = data["CapacityProviderArn"]
    else:
        raise DeserializationError("CapacityProvider.capacity_provider_arn required")
    if "State" in data:
        import capo_lambda.types.capacity_provider_state

        out["state"] = capo_lambda.types.capacity_provider_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("CapacityProvider.state required")
    if "VpcConfig" in data:
        import capo_lambda.types.capacity_provider_vpc_config

        out["vpc_config"] = (
            capo_lambda.types.capacity_provider_vpc_config.deserialize_json(
                data["VpcConfig"]
            )
        )
    else:
        raise DeserializationError("CapacityProvider.vpc_config required")
    if "PermissionsConfig" in data:
        import capo_lambda.types.capacity_provider_permissions_config

        out["permissions_config"] = (
            capo_lambda.types.capacity_provider_permissions_config.deserialize_json(
                data["PermissionsConfig"]
            )
        )
    else:
        raise DeserializationError("CapacityProvider.permissions_config required")
    if "InstanceRequirements" in data:
        import capo_lambda.types.instance_requirements

        out["instance_requirements"] = (
            capo_lambda.types.instance_requirements.deserialize_json(
                data["InstanceRequirements"]
            )
        )
    if "CapacityProviderScalingConfig" in data:
        import capo_lambda.types.capacity_provider_scaling_config

        out["capacity_provider_scaling_config"] = (
            capo_lambda.types.capacity_provider_scaling_config.deserialize_json(
                data["CapacityProviderScalingConfig"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "LastModified" in data:
        out["last_modified"] = data["LastModified"]
    return out
