"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.managed_vpc_resource
    import capo_bedrock_agentcore_control.types.self_managed_lattice_resource


class _PrivateEndpoint_selfManagedLatticeResource(TypedDict, closed=True):
    selfManagedLatticeResource: "capo_bedrock_agentcore_control.types.self_managed_lattice_resource.SelfManagedLatticeResource"


class _PrivateEndpoint_managedVpcResource(TypedDict, closed=True):
    managedVpcResource: (
        "capo_bedrock_agentcore_control.types.managed_vpc_resource.ManagedVpcResource"
    )


PrivateEndpoint: TypeAlias = (
    _PrivateEndpoint_selfManagedLatticeResource | _PrivateEndpoint_managedVpcResource
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpoint) -> dict:
    if "selfManagedLatticeResource" in value:
        import capo_bedrock_agentcore_control.types.self_managed_lattice_resource

        return {
            "selfManagedLatticeResource": capo_bedrock_agentcore_control.types.self_managed_lattice_resource.serialize_json(
                value["selfManagedLatticeResource"]
            )
        }
    elif "managedVpcResource" in value:
        import capo_bedrock_agentcore_control.types.managed_vpc_resource

        return {
            "managedVpcResource": capo_bedrock_agentcore_control.types.managed_vpc_resource.serialize_json(
                value["managedVpcResource"]
            )
        }
    else:
        raise SerializationError("PrivateEndpoint: no variant present")


def deserialize_json(data: dict) -> PrivateEndpoint:
    if "selfManagedLatticeResource" in data:
        import capo_bedrock_agentcore_control.types.self_managed_lattice_resource

        return {
            "selfManagedLatticeResource": capo_bedrock_agentcore_control.types.self_managed_lattice_resource.deserialize_json(
                data["selfManagedLatticeResource"]
            )
        }
    elif "managedVpcResource" in data:
        import capo_bedrock_agentcore_control.types.managed_vpc_resource

        return {
            "managedVpcResource": capo_bedrock_agentcore_control.types.managed_vpc_resource.deserialize_json(
                data["managedVpcResource"]
            )
        }
    else:
        raise DeserializationError("PrivateEndpoint: no recognized variant key")
