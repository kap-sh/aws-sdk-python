"""Generated from Smithy shape ``com.amazonaws.greengrass#ResourceDataContainer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.local_device_resource_data
    import aws_sdk_greengrass.types.local_volume_resource_data
    import aws_sdk_greengrass.types.s3_machine_learning_model_resource_data
    import aws_sdk_greengrass.types.sage_maker_machine_learning_model_resource_data
    import aws_sdk_greengrass.types.secrets_manager_secret_resource_data


class ResourceDataContainer(TypedDict):
    local_device_resource_data: NotRequired[
        "aws_sdk_greengrass.types.local_device_resource_data.LocalDeviceResourceData"
    ]
    """Attributes that define the local device resource."""
    local_volume_resource_data: NotRequired[
        "aws_sdk_greengrass.types.local_volume_resource_data.LocalVolumeResourceData"
    ]
    """Attributes that define the local volume resource."""
    s3_machine_learning_model_resource_data: NotRequired[
        "aws_sdk_greengrass.types.s3_machine_learning_model_resource_data.S3MachineLearningModelResourceData"
    ]
    """Attributes that define an Amazon S3 machine learning resource."""
    sage_maker_machine_learning_model_resource_data: NotRequired[
        "aws_sdk_greengrass.types.sage_maker_machine_learning_model_resource_data.SageMakerMachineLearningModelResourceData"
    ]
    """Attributes that define an Amazon SageMaker machine learning resource."""
    secrets_manager_secret_resource_data: NotRequired[
        "aws_sdk_greengrass.types.secrets_manager_secret_resource_data.SecretsManagerSecretResourceData"
    ]
    """Attributes that define a secret resource, which references a secret from AWS Secrets Manager."""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDataContainer) -> dict:
    out: dict = {}
    if "local_device_resource_data" in value:
        import aws_sdk_greengrass.types.local_device_resource_data

        out["LocalDeviceResourceData"] = (
            aws_sdk_greengrass.types.local_device_resource_data.serialize_json(
                value["local_device_resource_data"]
            )
        )
    if "local_volume_resource_data" in value:
        import aws_sdk_greengrass.types.local_volume_resource_data

        out["LocalVolumeResourceData"] = (
            aws_sdk_greengrass.types.local_volume_resource_data.serialize_json(
                value["local_volume_resource_data"]
            )
        )
    if "s3_machine_learning_model_resource_data" in value:
        import aws_sdk_greengrass.types.s3_machine_learning_model_resource_data

        out["S3MachineLearningModelResourceData"] = (
            aws_sdk_greengrass.types.s3_machine_learning_model_resource_data.serialize_json(
                value["s3_machine_learning_model_resource_data"]
            )
        )
    if "sage_maker_machine_learning_model_resource_data" in value:
        import aws_sdk_greengrass.types.sage_maker_machine_learning_model_resource_data

        out["SageMakerMachineLearningModelResourceData"] = (
            aws_sdk_greengrass.types.sage_maker_machine_learning_model_resource_data.serialize_json(
                value["sage_maker_machine_learning_model_resource_data"]
            )
        )
    if "secrets_manager_secret_resource_data" in value:
        import aws_sdk_greengrass.types.secrets_manager_secret_resource_data

        out["SecretsManagerSecretResourceData"] = (
            aws_sdk_greengrass.types.secrets_manager_secret_resource_data.serialize_json(
                value["secrets_manager_secret_resource_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceDataContainer:
    out: ResourceDataContainer = {}  # type: ignore[typeddict-item]
    if "LocalDeviceResourceData" in data:
        import aws_sdk_greengrass.types.local_device_resource_data

        out["local_device_resource_data"] = (
            aws_sdk_greengrass.types.local_device_resource_data.deserialize_json(
                data["LocalDeviceResourceData"]
            )
        )
    if "LocalVolumeResourceData" in data:
        import aws_sdk_greengrass.types.local_volume_resource_data

        out["local_volume_resource_data"] = (
            aws_sdk_greengrass.types.local_volume_resource_data.deserialize_json(
                data["LocalVolumeResourceData"]
            )
        )
    if "S3MachineLearningModelResourceData" in data:
        import aws_sdk_greengrass.types.s3_machine_learning_model_resource_data

        out["s3_machine_learning_model_resource_data"] = (
            aws_sdk_greengrass.types.s3_machine_learning_model_resource_data.deserialize_json(
                data["S3MachineLearningModelResourceData"]
            )
        )
    if "SageMakerMachineLearningModelResourceData" in data:
        import aws_sdk_greengrass.types.sage_maker_machine_learning_model_resource_data

        out["sage_maker_machine_learning_model_resource_data"] = (
            aws_sdk_greengrass.types.sage_maker_machine_learning_model_resource_data.deserialize_json(
                data["SageMakerMachineLearningModelResourceData"]
            )
        )
    if "SecretsManagerSecretResourceData" in data:
        import aws_sdk_greengrass.types.secrets_manager_secret_resource_data

        out["secrets_manager_secret_resource_data"] = (
            aws_sdk_greengrass.types.secrets_manager_secret_resource_data.deserialize_json(
                data["SecretsManagerSecretResourceData"]
            )
        )
    return out
