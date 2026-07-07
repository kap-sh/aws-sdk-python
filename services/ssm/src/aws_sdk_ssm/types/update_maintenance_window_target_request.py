"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateMaintenanceWindowTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.maintenance_window_description
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_name
    import aws_sdk_ssm.types.maintenance_window_target_id
    import aws_sdk_ssm.types.owner_information
    import aws_sdk_ssm.types.targets


class UpdateMaintenanceWindowTargetRequest(TypedDict, closed=True):
    window_id: "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The maintenance window ID with which to modify the target.</p>"""
    window_target_id: (
        "aws_sdk_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId"
    )
    """<p>The target ID to modify.</p>"""
    targets: NotRequired["aws_sdk_ssm.types.targets.Targets"]
    """<p>The targets to add or replace.</p>"""
    owner_information: NotRequired[
        "aws_sdk_ssm.types.owner_information.OwnerInformation"
    ]
    """<p>User-provided value that will be included in any Amazon CloudWatch Events events raised while running tasks for these targets in this maintenance window.</p>"""
    name: NotRequired["aws_sdk_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>A name for the update.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>An optional description for the update.</p>"""
    replace: NotRequired["aws_sdk_ssm.types.boolean.Boolean"]
    """<p>If <code>True</code>, then all fields that are required by the <a>RegisterTargetWithMaintenanceWindow</a> operation are also required for this API request. Optional fields that aren't specified are set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMaintenanceWindowTargetRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    out["WindowTargetId"] = value["window_target_id"]
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
    if "replace" in value:
        out["Replace"] = value["replace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMaintenanceWindowTargetRequest:
    out: UpdateMaintenanceWindowTargetRequest = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError(
            "UpdateMaintenanceWindowTargetRequest.window_id required"
        )
    if "WindowTargetId" in data:
        out["window_target_id"] = data["WindowTargetId"]
    else:
        raise DeserializationError(
            "UpdateMaintenanceWindowTargetRequest.window_target_id required"
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
    if "Replace" in data:
        out["replace"] = data["Replace"]
    return out
