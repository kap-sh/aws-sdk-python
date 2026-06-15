"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.managed_vpc_resource
    import aws_sdk_bedrock_agentcore_control.types.self_managed_lattice_resource


class _PrivateEndpoint_selfManagedLatticeResource(TypedDict):
    selfManagedLatticeResource: "aws_sdk_bedrock_agentcore_control.types.self_managed_lattice_resource.SelfManagedLatticeResource"


class _PrivateEndpoint_managedVpcResource(TypedDict):
    managedVpcResource: "aws_sdk_bedrock_agentcore_control.types.managed_vpc_resource.ManagedVpcResource"


PrivateEndpoint: TypeAlias = (
    _PrivateEndpoint_selfManagedLatticeResource | _PrivateEndpoint_managedVpcResource
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpoint) -> dict:
    if "selfManagedLatticeResource" in value:
        import aws_sdk_bedrock_agentcore_control.types.self_managed_lattice_resource

        return {
            "selfManagedLatticeResource": aws_sdk_bedrock_agentcore_control.types.self_managed_lattice_resource.serialize_json(
                value["selfManagedLatticeResource"]
            )
        }
    elif "managedVpcResource" in value:
        import aws_sdk_bedrock_agentcore_control.types.managed_vpc_resource

        return {
            "managedVpcResource": aws_sdk_bedrock_agentcore_control.types.managed_vpc_resource.serialize_json(
                value["managedVpcResource"]
            )
        }
    else:
        raise SerializationError("PrivateEndpoint: no variant present")


def deserialize_json(data: dict) -> PrivateEndpoint:
    if "selfManagedLatticeResource" in data:
        import aws_sdk_bedrock_agentcore_control.types.self_managed_lattice_resource

        return {
            "selfManagedLatticeResource": aws_sdk_bedrock_agentcore_control.types.self_managed_lattice_resource.deserialize_json(
                data["selfManagedLatticeResource"]
            )
        }
    elif "managedVpcResource" in data:
        import aws_sdk_bedrock_agentcore_control.types.managed_vpc_resource

        return {
            "managedVpcResource": aws_sdk_bedrock_agentcore_control.types.managed_vpc_resource.deserialize_json(
                data["managedVpcResource"]
            )
        }
    else:
        raise DeserializationError("PrivateEndpoint: no recognized variant key")
