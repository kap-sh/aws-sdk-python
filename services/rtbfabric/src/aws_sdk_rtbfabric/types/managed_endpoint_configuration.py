"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ManagedEndpointConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.auto_scaling_groups_configuration
    import aws_sdk_rtbfabric.types.eks_endpoints_configuration


class _ManagedEndpointConfiguration_autoScalingGroups(TypedDict):
    autoScalingGroups: "aws_sdk_rtbfabric.types.auto_scaling_groups_configuration.AutoScalingGroupsConfiguration"


class _ManagedEndpointConfiguration_eksEndpoints(TypedDict):
    eksEndpoints: (
        "aws_sdk_rtbfabric.types.eks_endpoints_configuration.EksEndpointsConfiguration"
    )


ManagedEndpointConfiguration: TypeAlias = (
    _ManagedEndpointConfiguration_autoScalingGroups
    | _ManagedEndpointConfiguration_eksEndpoints
)


# --- restJson1 ser/de ---
def serialize_json(value: ManagedEndpointConfiguration) -> dict:
    if "autoScalingGroups" in value:
        import aws_sdk_rtbfabric.types.auto_scaling_groups_configuration

        return {
            "autoScalingGroups": aws_sdk_rtbfabric.types.auto_scaling_groups_configuration.serialize_json(
                value["autoScalingGroups"]
            )
        }
    elif "eksEndpoints" in value:
        import aws_sdk_rtbfabric.types.eks_endpoints_configuration

        return {
            "eksEndpoints": aws_sdk_rtbfabric.types.eks_endpoints_configuration.serialize_json(
                value["eksEndpoints"]
            )
        }
    else:
        raise SerializationError("ManagedEndpointConfiguration: no variant present")


def deserialize_json(data: dict) -> ManagedEndpointConfiguration:
    if "autoScalingGroups" in data:
        import aws_sdk_rtbfabric.types.auto_scaling_groups_configuration

        return {
            "autoScalingGroups": aws_sdk_rtbfabric.types.auto_scaling_groups_configuration.deserialize_json(
                data["autoScalingGroups"]
            )
        }
    elif "eksEndpoints" in data:
        import aws_sdk_rtbfabric.types.eks_endpoints_configuration

        return {
            "eksEndpoints": aws_sdk_rtbfabric.types.eks_endpoints_configuration.deserialize_json(
                data["eksEndpoints"]
            )
        }
    else:
        raise DeserializationError(
            "ManagedEndpointConfiguration: no recognized variant key"
        )
