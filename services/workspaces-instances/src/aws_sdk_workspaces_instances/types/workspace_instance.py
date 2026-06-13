"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#WorkspaceInstance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.ec2_managed_instance
    import aws_sdk_workspaces_instances.types.provision_state_enum
    import aws_sdk_workspaces_instances.types.workspace_instance_id


class WorkspaceInstance(TypedDict):
    provision_state: NotRequired[
        "aws_sdk_workspaces_instances.types.provision_state_enum.ProvisionStateEnum"
    ]
    """<p>Current provisioning state of the WorkSpace Instance.</p>"""
    workspace_instance_id: NotRequired[
        "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    ]
    """<p>Unique identifier for the WorkSpace Instance.</p>"""
    ec2_managed_instance: NotRequired[
        "aws_sdk_workspaces_instances.types.ec2_managed_instance.EC2ManagedInstance"
    ]
    """<p>Details of the associated EC2 managed instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkspaceInstance) -> dict:
    out: dict = {}
    if "provision_state" in value:
        import aws_sdk_workspaces_instances.types.provision_state_enum

        out["ProvisionState"] = (
            aws_sdk_workspaces_instances.types.provision_state_enum.serialize_aws_json_1_0(
                value["provision_state"]
            )
        )
    if "workspace_instance_id" in value:
        out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    if "ec2_managed_instance" in value:
        import aws_sdk_workspaces_instances.types.ec2_managed_instance

        out["EC2ManagedInstance"] = (
            aws_sdk_workspaces_instances.types.ec2_managed_instance.serialize_aws_json_1_0(
                value["ec2_managed_instance"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkspaceInstance:
    out: WorkspaceInstance = {}  # type: ignore[typeddict-item]
    if "ProvisionState" in data:
        import aws_sdk_workspaces_instances.types.provision_state_enum

        out["provision_state"] = (
            aws_sdk_workspaces_instances.types.provision_state_enum.deserialize_aws_json_1_0(
                data["ProvisionState"]
            )
        )
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    if "EC2ManagedInstance" in data:
        import aws_sdk_workspaces_instances.types.ec2_managed_instance

        out["ec2_managed_instance"] = (
            aws_sdk_workspaces_instances.types.ec2_managed_instance.deserialize_aws_json_1_0(
                data["EC2ManagedInstance"]
            )
        )
    return out
