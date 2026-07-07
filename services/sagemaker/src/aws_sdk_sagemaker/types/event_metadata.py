"""Generated from Smithy shape ``com.amazonaws.sagemaker#EventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_metadata
    import aws_sdk_sagemaker.types.instance_group_metadata
    import aws_sdk_sagemaker.types.instance_group_scaling_metadata
    import aws_sdk_sagemaker.types.instance_metadata


class _EventMetadata_Cluster(TypedDict, closed=True):
    Cluster: "aws_sdk_sagemaker.types.cluster_metadata.ClusterMetadata"


class _EventMetadata_InstanceGroup(TypedDict, closed=True):
    InstanceGroup: (
        "aws_sdk_sagemaker.types.instance_group_metadata.InstanceGroupMetadata"
    )


class _EventMetadata_InstanceGroupScaling(TypedDict, closed=True):
    InstanceGroupScaling: "aws_sdk_sagemaker.types.instance_group_scaling_metadata.InstanceGroupScalingMetadata"


class _EventMetadata_Instance(TypedDict, closed=True):
    Instance: "aws_sdk_sagemaker.types.instance_metadata.InstanceMetadata"


EventMetadata: TypeAlias = (
    _EventMetadata_Cluster
    | _EventMetadata_InstanceGroup
    | _EventMetadata_InstanceGroupScaling
    | _EventMetadata_Instance
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventMetadata) -> dict:
    if "Cluster" in value:
        import aws_sdk_sagemaker.types.cluster_metadata

        return {
            "Cluster": aws_sdk_sagemaker.types.cluster_metadata.serialize_aws_json_1_1(
                value["Cluster"]
            )
        }
    elif "InstanceGroup" in value:
        import aws_sdk_sagemaker.types.instance_group_metadata

        return {
            "InstanceGroup": aws_sdk_sagemaker.types.instance_group_metadata.serialize_aws_json_1_1(
                value["InstanceGroup"]
            )
        }
    elif "InstanceGroupScaling" in value:
        import aws_sdk_sagemaker.types.instance_group_scaling_metadata

        return {
            "InstanceGroupScaling": aws_sdk_sagemaker.types.instance_group_scaling_metadata.serialize_aws_json_1_1(
                value["InstanceGroupScaling"]
            )
        }
    elif "Instance" in value:
        import aws_sdk_sagemaker.types.instance_metadata

        return {
            "Instance": aws_sdk_sagemaker.types.instance_metadata.serialize_aws_json_1_1(
                value["Instance"]
            )
        }
    else:
        raise SerializationError("EventMetadata: no variant present")


def deserialize_aws_json_1_1(data: dict) -> EventMetadata:
    if "Cluster" in data:
        import aws_sdk_sagemaker.types.cluster_metadata

        return {
            "Cluster": aws_sdk_sagemaker.types.cluster_metadata.deserialize_aws_json_1_1(
                data["Cluster"]
            )
        }
    elif "InstanceGroup" in data:
        import aws_sdk_sagemaker.types.instance_group_metadata

        return {
            "InstanceGroup": aws_sdk_sagemaker.types.instance_group_metadata.deserialize_aws_json_1_1(
                data["InstanceGroup"]
            )
        }
    elif "InstanceGroupScaling" in data:
        import aws_sdk_sagemaker.types.instance_group_scaling_metadata

        return {
            "InstanceGroupScaling": aws_sdk_sagemaker.types.instance_group_scaling_metadata.deserialize_aws_json_1_1(
                data["InstanceGroupScaling"]
            )
        }
    elif "Instance" in data:
        import aws_sdk_sagemaker.types.instance_metadata

        return {
            "Instance": aws_sdk_sagemaker.types.instance_metadata.deserialize_aws_json_1_1(
                data["Instance"]
            )
        }
    else:
        raise DeserializationError("EventMetadata: no recognized variant key")
