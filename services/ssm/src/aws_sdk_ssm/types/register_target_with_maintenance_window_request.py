"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterTargetWithMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.client_token
    import aws_sdk_ssm.types.maintenance_window_description
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_name
    import aws_sdk_ssm.types.maintenance_window_resource_type
    import aws_sdk_ssm.types.owner_information
    import aws_sdk_ssm.types.targets


class RegisterTargetWithMaintenanceWindowRequest(TypedDict):
    window_id: "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window the target should be registered with.</p>"""
    resource_type: "aws_sdk_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType"
    """<p>The type of target being registered with the maintenance window.</p>"""
    targets: "aws_sdk_ssm.types.targets.Targets"
    r"""<p>The targets to register with the maintenance window. In other words, the managed nodes to run commands on when the maintenance window runs.</p> <note> <p>If a single maintenance window task is registered with multiple targets, its task invocations occur sequentially and not in parallel. If your task must run on multiple targets at the same time, register a task for each target individually and assign each task the same priority level.</p> </note> <p>You can specify targets using managed node IDs, resource group names, or tags that have been applied to managed nodes.</p> <p> <b>Example 1</b>: Specify managed node IDs</p> <p> <code>Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>,<instance-id-3></code> </p> <p> <b>Example 2</b>: Use tag key-pairs applied to managed nodes</p> <p> <code>Key=tag:<my-tag-key>,Values=<my-tag-value-1>,<my-tag-value-2></code> </p> <p> <b>Example 3</b>: Use tag-keys applied to managed nodes</p> <p> <code>Key=tag-key,Values=<my-tag-key-1>,<my-tag-key-2></code> </p> <p> <b>Example 4</b>: Use resource group names</p> <p> <code>Key=resource-groups:Name,Values=<resource-group-name></code> </p> <p> <b>Example 5</b>: Use filters for resource group types</p> <p> <code>Key=resource-groups:ResourceTypeFilters,Values=<resource-type-1>,<resource-type-2></code> </p> <note> <p>For <code>Key=resource-groups:ResourceTypeFilters</code>, specify resource types in the following format</p> <p> <code>Key=resource-groups:ResourceTypeFilters,Values=AWS::EC2::INSTANCE,AWS::EC2::VPC</code> </p> </note> <p>For more information about these examples formats, including the best use case for each one, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html\">Examples: Register targets with a maintenance window</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    owner_information: NotRequired[
        "aws_sdk_ssm.types.owner_information.OwnerInformation"
    ]
    """<p>User-provided value that will be included in any Amazon CloudWatch Events events raised while running tasks for these targets in this maintenance window.</p>"""
    name: NotRequired["aws_sdk_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>An optional name for the target.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>An optional description for the target.</p>"""
    client_token: NotRequired["aws_sdk_ssm.types.client_token.ClientToken"]
    """<p>User-provided idempotency token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterTargetWithMaintenanceWindowRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    import aws_sdk_ssm.types.maintenance_window_resource_type

    out["ResourceType"] = (
        aws_sdk_ssm.types.maintenance_window_resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    import aws_sdk_ssm.types.targets

    out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "owner_information" in value:
        out["OwnerInformation"] = value["owner_information"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterTargetWithMaintenanceWindowRequest:
    out: RegisterTargetWithMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError(
            "RegisterTargetWithMaintenanceWindowRequest.window_id required"
        )
    if "ResourceType" in data:
        import aws_sdk_ssm.types.maintenance_window_resource_type

        out["resource_type"] = (
            aws_sdk_ssm.types.maintenance_window_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterTargetWithMaintenanceWindowRequest.resource_type required"
        )
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    else:
        raise DeserializationError(
            "RegisterTargetWithMaintenanceWindowRequest.targets required"
        )
    if "OwnerInformation" in data:
        out["owner_information"] = data["OwnerInformation"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
