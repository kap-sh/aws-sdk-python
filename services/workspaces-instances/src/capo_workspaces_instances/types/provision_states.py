"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ProvisionStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.provision_state_enum

ProvisionStates: TypeAlias = list[
    "capo_workspaces_instances.types.provision_state_enum.ProvisionStateEnum"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionStates) -> list:
    import capo_workspaces_instances.types.provision_state_enum

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.provision_state_enum.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProvisionStates:
    import capo_workspaces_instances.types.provision_state_enum

    out: ProvisionStates = []
    for item in data:
        out.append(
            capo_workspaces_instances.types.provision_state_enum.deserialize_aws_json_1_0(
                item
            )
        )
    return out
