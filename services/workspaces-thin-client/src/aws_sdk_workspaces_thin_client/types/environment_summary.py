"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#EnvironmentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.activation_code
    import aws_sdk_workspaces_thin_client.types.arn
    import aws_sdk_workspaces_thin_client.types.desktop_endpoint
    import aws_sdk_workspaces_thin_client.types.desktop_type
    import aws_sdk_workspaces_thin_client.types.environment_id
    import aws_sdk_workspaces_thin_client.types.environment_name
    import aws_sdk_workspaces_thin_client.types.maintenance_window
    import aws_sdk_workspaces_thin_client.types.software_set_id
    import aws_sdk_workspaces_thin_client.types.software_set_update_mode
    import aws_sdk_workspaces_thin_client.types.software_set_update_schedule
    import aws_sdk_workspaces_thin_client.types.timestamp


class EnvironmentSummary(TypedDict):
    id: NotRequired["aws_sdk_workspaces_thin_client.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment.</p>"""
    name: NotRequired[
        "aws_sdk_workspaces_thin_client.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment.</p>"""
    desktop_arn: NotRequired["aws_sdk_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or AppStream 2.0.</p>"""
    desktop_endpoint: NotRequired[
        "aws_sdk_workspaces_thin_client.types.desktop_endpoint.DesktopEndpoint"
    ]
    """<p>The URL for the identity provider login (only for environments that use AppStream 2.0).</p>"""
    desktop_type: NotRequired[
        "aws_sdk_workspaces_thin_client.types.desktop_type.DesktopType"
    ]
    """<p>The type of streaming desktop for the environment.</p>"""
    activation_code: NotRequired[
        "aws_sdk_workspaces_thin_client.types.activation_code.ActivationCode"
    ]
    """<p>The activation code to register a device to the environment.</p>"""
    software_set_update_schedule: NotRequired[
        "aws_sdk_workspaces_thin_client.types.software_set_update_schedule.SoftwareSetUpdateSchedule"
    ]
    """<p>An option to define if software updates should be applied within a maintenance window.</p>"""
    maintenance_window: NotRequired[
        "aws_sdk_workspaces_thin_client.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>A specification for a time window to apply software updates.</p>"""
    software_set_update_mode: NotRequired[
        "aws_sdk_workspaces_thin_client.types.software_set_update_mode.SoftwareSetUpdateMode"
    ]
    """<p>An option to define which software updates to apply.</p>"""
    desired_software_set_id: NotRequired[
        "aws_sdk_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set to apply.</p>"""
    pending_software_set_id: NotRequired[
        "aws_sdk_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set that is pending to be installed.</p>"""
    created_at: NotRequired["aws_sdk_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the environment was created.</p>"""
    updated_at: NotRequired["aws_sdk_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the device was updated.</p>"""
    arn: NotRequired["aws_sdk_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "desktop_arn" in value:
        out["desktopArn"] = value["desktop_arn"]
    if "desktop_endpoint" in value:
        out["desktopEndpoint"] = value["desktop_endpoint"]
    if "desktop_type" in value:
        import aws_sdk_workspaces_thin_client.types.desktop_type

        out["desktopType"] = (
            aws_sdk_workspaces_thin_client.types.desktop_type.serialize_json(
                value["desktop_type"]
            )
        )
    if "activation_code" in value:
        out["activationCode"] = value["activation_code"]
    if "software_set_update_schedule" in value:
        import aws_sdk_workspaces_thin_client.types.software_set_update_schedule

        out["softwareSetUpdateSchedule"] = (
            aws_sdk_workspaces_thin_client.types.software_set_update_schedule.serialize_json(
                value["software_set_update_schedule"]
            )
        )
    if "maintenance_window" in value:
        import aws_sdk_workspaces_thin_client.types.maintenance_window

        out["maintenanceWindow"] = (
            aws_sdk_workspaces_thin_client.types.maintenance_window.serialize_json(
                value["maintenance_window"]
            )
        )
    if "software_set_update_mode" in value:
        import aws_sdk_workspaces_thin_client.types.software_set_update_mode

        out["softwareSetUpdateMode"] = (
            aws_sdk_workspaces_thin_client.types.software_set_update_mode.serialize_json(
                value["software_set_update_mode"]
            )
        )
    if "desired_software_set_id" in value:
        out["desiredSoftwareSetId"] = value["desired_software_set_id"]
    if "pending_software_set_id" in value:
        out["pendingSoftwareSetId"] = value["pending_software_set_id"]
    if "created_at" in value:
        import aws_sdk_workspaces_thin_client.types.timestamp

        out["createdAt"] = (
            aws_sdk_workspaces_thin_client.types.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_workspaces_thin_client.types.timestamp

        out["updatedAt"] = (
            aws_sdk_workspaces_thin_client.types.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> EnvironmentSummary:
    out: EnvironmentSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "desktopArn" in data:
        out["desktop_arn"] = data["desktopArn"]
    if "desktopEndpoint" in data:
        out["desktop_endpoint"] = data["desktopEndpoint"]
    if "desktopType" in data:
        import aws_sdk_workspaces_thin_client.types.desktop_type

        out["desktop_type"] = (
            aws_sdk_workspaces_thin_client.types.desktop_type.deserialize_json(
                data["desktopType"]
            )
        )
    if "activationCode" in data:
        out["activation_code"] = data["activationCode"]
    if "softwareSetUpdateSchedule" in data:
        import aws_sdk_workspaces_thin_client.types.software_set_update_schedule

        out["software_set_update_schedule"] = (
            aws_sdk_workspaces_thin_client.types.software_set_update_schedule.deserialize_json(
                data["softwareSetUpdateSchedule"]
            )
        )
    if "maintenanceWindow" in data:
        import aws_sdk_workspaces_thin_client.types.maintenance_window

        out["maintenance_window"] = (
            aws_sdk_workspaces_thin_client.types.maintenance_window.deserialize_json(
                data["maintenanceWindow"]
            )
        )
    if "softwareSetUpdateMode" in data:
        import aws_sdk_workspaces_thin_client.types.software_set_update_mode

        out["software_set_update_mode"] = (
            aws_sdk_workspaces_thin_client.types.software_set_update_mode.deserialize_json(
                data["softwareSetUpdateMode"]
            )
        )
    if "desiredSoftwareSetId" in data:
        out["desired_software_set_id"] = data["desiredSoftwareSetId"]
    if "pendingSoftwareSetId" in data:
        out["pending_software_set_id"] = data["pendingSoftwareSetId"]
    if "createdAt" in data:
        import aws_sdk_workspaces_thin_client.types.timestamp

        out["created_at"] = (
            aws_sdk_workspaces_thin_client.types.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_workspaces_thin_client.types.timestamp

        out["updated_at"] = (
            aws_sdk_workspaces_thin_client.types.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
