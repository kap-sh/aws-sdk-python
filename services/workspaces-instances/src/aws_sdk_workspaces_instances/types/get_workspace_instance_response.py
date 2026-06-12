"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#GetWorkspaceInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.billing_configuration
    import aws_sdk_workspaces_instances.types.ec2_instance_errors
    import aws_sdk_workspaces_instances.types.ec2_managed_instance
    import aws_sdk_workspaces_instances.types.provision_state_enum
    import aws_sdk_workspaces_instances.types.workspace_instance_errors
    import aws_sdk_workspaces_instances.types.workspace_instance_id

class GetWorkspaceInstanceResponse(TypedDict):
    workspace_instance_errors: NotRequired["aws_sdk_workspaces_instances.types.workspace_instance_errors.WorkspaceInstanceErrors"]
    """<p>Captures any errors specific to the WorkSpace Instance lifecycle.</p>"""
    ec2_instance_errors: NotRequired["aws_sdk_workspaces_instances.types.ec2_instance_errors.EC2InstanceErrors"]
    """<p>Includes any underlying EC2 instance errors encountered.</p>"""
    provision_state: NotRequired["aws_sdk_workspaces_instances.types.provision_state_enum.ProvisionStateEnum"]
    """<p>Current provisioning state of the WorkSpaces Instance.</p>"""
    workspace_instance_id: NotRequired["aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"]
    """<p>Unique identifier of the retrieved WorkSpaces Instance.</p>"""
    ec2_managed_instance: NotRequired["aws_sdk_workspaces_instances.types.ec2_managed_instance.EC2ManagedInstance"]
    """<p>Details of the associated EC2 managed instance.</p>"""
    billing_configuration: NotRequired["aws_sdk_workspaces_instances.types.billing_configuration.BillingConfiguration"]
    """<p>Returns the current billing configuration for the WorkSpace Instance, indicating the active billing mode.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkspaceInstanceResponse) -> dict:
    out: dict = {}
    if "workspace_instance_errors" in value:
        import aws_sdk_workspaces_instances.types.workspace_instance_errors
        out["WorkspaceInstanceErrors"] = aws_sdk_workspaces_instances.types.workspace_instance_errors.serialize_aws_json_1_0(value["workspace_instance_errors"])
    if "ec2_instance_errors" in value:
        import aws_sdk_workspaces_instances.types.ec2_instance_errors
        out["EC2InstanceErrors"] = aws_sdk_workspaces_instances.types.ec2_instance_errors.serialize_aws_json_1_0(value["ec2_instance_errors"])
    if "provision_state" in value:
        import aws_sdk_workspaces_instances.types.provision_state_enum
        out["ProvisionState"] = aws_sdk_workspaces_instances.types.provision_state_enum.serialize_aws_json_1_0(value["provision_state"])
    if "workspace_instance_id" in value:
        out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    if "ec2_managed_instance" in value:
        import aws_sdk_workspaces_instances.types.ec2_managed_instance
        out["EC2ManagedInstance"] = aws_sdk_workspaces_instances.types.ec2_managed_instance.serialize_aws_json_1_0(value["ec2_managed_instance"])
    if "billing_configuration" in value:
        import aws_sdk_workspaces_instances.types.billing_configuration
        out["BillingConfiguration"] = aws_sdk_workspaces_instances.types.billing_configuration.serialize_aws_json_1_0(value["billing_configuration"])
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkspaceInstanceResponse:
    out: GetWorkspaceInstanceResponse = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstanceErrors" in data:
        import aws_sdk_workspaces_instances.types.workspace_instance_errors
        out["workspace_instance_errors"] = aws_sdk_workspaces_instances.types.workspace_instance_errors.deserialize_aws_json_1_0(data["WorkspaceInstanceErrors"])
    if "EC2InstanceErrors" in data:
        import aws_sdk_workspaces_instances.types.ec2_instance_errors
        out["ec2_instance_errors"] = aws_sdk_workspaces_instances.types.ec2_instance_errors.deserialize_aws_json_1_0(data["EC2InstanceErrors"])
    if "ProvisionState" in data:
        import aws_sdk_workspaces_instances.types.provision_state_enum
        out["provision_state"] = aws_sdk_workspaces_instances.types.provision_state_enum.deserialize_aws_json_1_0(data["ProvisionState"])
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    if "EC2ManagedInstance" in data:
        import aws_sdk_workspaces_instances.types.ec2_managed_instance
        out["ec2_managed_instance"] = aws_sdk_workspaces_instances.types.ec2_managed_instance.deserialize_aws_json_1_0(data["EC2ManagedInstance"])
    if "BillingConfiguration" in data:
        import aws_sdk_workspaces_instances.types.billing_configuration
        out["billing_configuration"] = aws_sdk_workspaces_instances.types.billing_configuration.deserialize_aws_json_1_0(data["BillingConfiguration"])
    return out