"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#Device``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.arn
    import capo_workspaces_thin_client.types.device_id
    import capo_workspaces_thin_client.types.device_name
    import capo_workspaces_thin_client.types.device_software_set_compliance_status
    import capo_workspaces_thin_client.types.device_status
    import capo_workspaces_thin_client.types.environment_id
    import capo_workspaces_thin_client.types.kms_key_arn
    import capo_workspaces_thin_client.types.software_set_id
    import capo_workspaces_thin_client.types.software_set_update_schedule
    import capo_workspaces_thin_client.types.software_set_update_status
    import capo_workspaces_thin_client.types.timestamp
    import capo_workspaces_thin_client.types.user_id


class Device(TypedDict, closed=True):
    id: NotRequired["capo_workspaces_thin_client.types.device_id.DeviceId"]
    """<p>The ID of the device.</p>"""
    serial_number: NotRequired["str"]
    """<p>The hardware serial number of the device.</p>"""
    name: NotRequired["capo_workspaces_thin_client.types.device_name.DeviceName"]
    """<p>The name of the device.</p>"""
    model: NotRequired["str"]
    """<p>The model number of the device.</p>"""
    environment_id: NotRequired[
        "capo_workspaces_thin_client.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment the device is associated with.</p>"""
    status: NotRequired["capo_workspaces_thin_client.types.device_status.DeviceStatus"]
    """<p>The status of the device.</p>"""
    current_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set currently installed on the device.</p>"""
    current_software_set_version: NotRequired["str"]
    """<p>The version of the software set currently installed on the device.</p>"""
    desired_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set which the device has been set to.</p>"""
    pending_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set that is pending to be installed on the device.</p>"""
    pending_software_set_version: NotRequired["str"]
    """<p>The version of the software set that is pending to be installed on the device.</p>"""
    software_set_update_schedule: NotRequired[
        "capo_workspaces_thin_client.types.software_set_update_schedule.SoftwareSetUpdateSchedule"
    ]
    """<p>An option to define if software updates should be applied within a maintenance window.</p>"""
    software_set_compliance_status: NotRequired[
        "capo_workspaces_thin_client.types.device_software_set_compliance_status.DeviceSoftwareSetComplianceStatus"
    ]
    """<p>Describes if the software currently installed on the device is a supported version.</p>"""
    software_set_update_status: NotRequired[
        "capo_workspaces_thin_client.types.software_set_update_status.SoftwareSetUpdateStatus"
    ]
    """<p>Describes if the device has a supported version of software installed.</p>"""
    last_connected_at: NotRequired[
        "capo_workspaces_thin_client.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the most recent session on the device.</p>"""
    last_posture_at: NotRequired[
        "capo_workspaces_thin_client.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the most recent check-in of the device.</p>"""
    created_at: NotRequired["capo_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the device was created.</p>"""
    updated_at: NotRequired["capo_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the device was updated.</p>"""
    arn: NotRequired["capo_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the device.</p>"""
    kms_key_arn: NotRequired["capo_workspaces_thin_client.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service key used to encrypt the device.</p>"""
    last_user_id: NotRequired["capo_workspaces_thin_client.types.user_id.UserId"]
    """<p>The user ID of the most recent session on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Device) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "serial_number" in value:
        out["serialNumber"] = value["serial_number"]
    if "name" in value:
        out["name"] = value["name"]
    if "model" in value:
        out["model"] = value["model"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "status" in value:
        import capo_workspaces_thin_client.types.device_status

        out["status"] = capo_workspaces_thin_client.types.device_status.serialize_json(
            value["status"]
        )
    if "current_software_set_id" in value:
        out["currentSoftwareSetId"] = value["current_software_set_id"]
    if "current_software_set_version" in value:
        out["currentSoftwareSetVersion"] = value["current_software_set_version"]
    if "desired_software_set_id" in value:
        out["desiredSoftwareSetId"] = value["desired_software_set_id"]
    if "pending_software_set_id" in value:
        out["pendingSoftwareSetId"] = value["pending_software_set_id"]
    if "pending_software_set_version" in value:
        out["pendingSoftwareSetVersion"] = value["pending_software_set_version"]
    if "software_set_update_schedule" in value:
        import capo_workspaces_thin_client.types.software_set_update_schedule

        out["softwareSetUpdateSchedule"] = (
            capo_workspaces_thin_client.types.software_set_update_schedule.serialize_json(
                value["software_set_update_schedule"]
            )
        )
    if "software_set_compliance_status" in value:
        import capo_workspaces_thin_client.types.device_software_set_compliance_status

        out["softwareSetComplianceStatus"] = (
            capo_workspaces_thin_client.types.device_software_set_compliance_status.serialize_json(
                value["software_set_compliance_status"]
            )
        )
    if "software_set_update_status" in value:
        import capo_workspaces_thin_client.types.software_set_update_status

        out["softwareSetUpdateStatus"] = (
            capo_workspaces_thin_client.types.software_set_update_status.serialize_json(
                value["software_set_update_status"]
            )
        )
    if "last_connected_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["lastConnectedAt"] = (
            capo_workspaces_thin_client.types.timestamp.serialize_json(
                value["last_connected_at"]
            )
        )
    if "last_posture_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["lastPostureAt"] = (
            capo_workspaces_thin_client.types.timestamp.serialize_json(
                value["last_posture_at"]
            )
        )
    if "created_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["createdAt"] = capo_workspaces_thin_client.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["updatedAt"] = capo_workspaces_thin_client.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "last_user_id" in value:
        out["lastUserId"] = value["last_user_id"]
    return out


def deserialize_json(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "serialNumber" in data:
        out["serial_number"] = data["serialNumber"]
    if "name" in data:
        out["name"] = data["name"]
    if "model" in data:
        out["model"] = data["model"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "status" in data:
        import capo_workspaces_thin_client.types.device_status

        out["status"] = (
            capo_workspaces_thin_client.types.device_status.deserialize_json(
                data["status"]
            )
        )
    if "currentSoftwareSetId" in data:
        out["current_software_set_id"] = data["currentSoftwareSetId"]
    if "currentSoftwareSetVersion" in data:
        out["current_software_set_version"] = data["currentSoftwareSetVersion"]
    if "desiredSoftwareSetId" in data:
        out["desired_software_set_id"] = data["desiredSoftwareSetId"]
    if "pendingSoftwareSetId" in data:
        out["pending_software_set_id"] = data["pendingSoftwareSetId"]
    if "pendingSoftwareSetVersion" in data:
        out["pending_software_set_version"] = data["pendingSoftwareSetVersion"]
    if "softwareSetUpdateSchedule" in data:
        import capo_workspaces_thin_client.types.software_set_update_schedule

        out["software_set_update_schedule"] = (
            capo_workspaces_thin_client.types.software_set_update_schedule.deserialize_json(
                data["softwareSetUpdateSchedule"]
            )
        )
    if "softwareSetComplianceStatus" in data:
        import capo_workspaces_thin_client.types.device_software_set_compliance_status

        out["software_set_compliance_status"] = (
            capo_workspaces_thin_client.types.device_software_set_compliance_status.deserialize_json(
                data["softwareSetComplianceStatus"]
            )
        )
    if "softwareSetUpdateStatus" in data:
        import capo_workspaces_thin_client.types.software_set_update_status

        out["software_set_update_status"] = (
            capo_workspaces_thin_client.types.software_set_update_status.deserialize_json(
                data["softwareSetUpdateStatus"]
            )
        )
    if "lastConnectedAt" in data:
        import capo_workspaces_thin_client.types.timestamp

        out["last_connected_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["lastConnectedAt"]
            )
        )
    if "lastPostureAt" in data:
        import capo_workspaces_thin_client.types.timestamp

        out["last_posture_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["lastPostureAt"]
            )
        )
    if "createdAt" in data:
        import capo_workspaces_thin_client.types.timestamp

        out["created_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_workspaces_thin_client.types.timestamp

        out["updated_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "lastUserId" in data:
        out["last_user_id"] = data["lastUserId"]
    return out
