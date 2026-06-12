"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CreateWorkspaceInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces_instances.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.billing_configuration
    import aws_sdk_workspaces_instances.types.client_token
    import aws_sdk_workspaces_instances.types.managed_instance_request
    import aws_sdk_workspaces_instances.types.tag_list

class CreateWorkspaceInstanceRequest(TypedDict):
    client_token: NotRequired["aws_sdk_workspaces_instances.types.client_token.ClientToken"]
    """<p>Unique token to ensure idempotent instance creation, preventing duplicate workspace launches.</p>"""
    tags: NotRequired["aws_sdk_workspaces_instances.types.tag_list.TagList"]
    """<p>Optional metadata tags for categorizing and managing WorkSpaces Instances.</p>"""
    managed_instance: "aws_sdk_workspaces_instances.types.managed_instance_request.ManagedInstanceRequest"
    """<p>Comprehensive configuration settings for the WorkSpaces Instance, including network, compute, and storage parameters.</p>"""
    billing_configuration: NotRequired["aws_sdk_workspaces_instances.types.billing_configuration.BillingConfiguration"]
    """<p>Optional billing configuration for the WorkSpace Instance. Allows customers to specify their preferred billing mode when creating a new instance. Defaults to hourly billing if not specified.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWorkspaceInstanceRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_workspaces_instances.types.tag_list
        out["Tags"] = aws_sdk_workspaces_instances.types.tag_list.serialize_aws_json_1_0(value["tags"])
    import aws_sdk_workspaces_instances.types.managed_instance_request
    out["ManagedInstance"] = aws_sdk_workspaces_instances.types.managed_instance_request.serialize_aws_json_1_0(value["managed_instance"])
    if "billing_configuration" in value:
        import aws_sdk_workspaces_instances.types.billing_configuration
        out["BillingConfiguration"] = aws_sdk_workspaces_instances.types.billing_configuration.serialize_aws_json_1_0(value["billing_configuration"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWorkspaceInstanceRequest:
    out: CreateWorkspaceInstanceRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_workspaces_instances.types.tag_list
        out["tags"] = aws_sdk_workspaces_instances.types.tag_list.deserialize_aws_json_1_0(data["Tags"])
    if "ManagedInstance" in data:
        import aws_sdk_workspaces_instances.types.managed_instance_request
        out["managed_instance"] = aws_sdk_workspaces_instances.types.managed_instance_request.deserialize_aws_json_1_0(data["ManagedInstance"])
    else:
        raise DeserializationError("CreateWorkspaceInstanceRequest.managed_instance required")
    if "BillingConfiguration" in data:
        import aws_sdk_workspaces_instances.types.billing_configuration
        out["billing_configuration"] = aws_sdk_workspaces_instances.types.billing_configuration.deserialize_aws_json_1_0(data["BillingConfiguration"])
    return out