"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_description
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_name
    import aws_sdk_ssm.types.maintenance_window_resource_type
    import aws_sdk_ssm.types.maintenance_window_target_id
    import aws_sdk_ssm.types.owner_information
    import aws_sdk_ssm.types.targets


class MaintenanceWindowTarget(TypedDict):
    window_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    ]
    """<p>The ID of the maintenance window to register the target with.</p>"""
    window_target_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId"
    ]
    """<p>The ID of the target.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType"
    ]
    """<p>The type of target that is being registered with the maintenance window.</p>"""
    targets: NotRequired["aws_sdk_ssm.types.targets.Targets"]
    """<p>The targets, either managed nodes or tags.</p> <p>Specify managed nodes using the following format:</p> <p> <code>Key=instanceids,Values=<instanceid1>,<instanceid2></code> </p> <p>Tags are specified using the following format:</p> <p> <code>Key=<tag name>,Values=<tag value></code>.</p>"""
    owner_information: NotRequired[
        "aws_sdk_ssm.types.owner_information.OwnerInformation"
    ]
    """<p>A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.</p>"""
    name: NotRequired["aws_sdk_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The name for the maintenance window target.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>A description for the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTarget) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "window_target_id" in value:
        out["WindowTargetId"] = value["window_target_id"]
    if "resource_type" in value:
        import aws_sdk_ssm.types.maintenance_window_resource_type

        out["ResourceType"] = (
            aws_sdk_ssm.types.maintenance_window_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "targets" in value:
        import aws_sdk_ssm.types.targets

        out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "owner_information" in value:
        out["OwnerInformation"] = value["owner_information"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowTarget:
    out: MaintenanceWindowTarget = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    if "WindowTargetId" in data:
        out["window_target_id"] = data["WindowTargetId"]
    if "ResourceType" in data:
        import aws_sdk_ssm.types.maintenance_window_resource_type

        out["resource_type"] = (
            aws_sdk_ssm.types.maintenance_window_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "OwnerInformation" in data:
        out["owner_information"] = data["OwnerInformation"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
