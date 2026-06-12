"""Generated from Smithy shape ``com.amazonaws.deadline#FleetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.auto_scaling_status
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_configuration
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.fleet_status
    import aws_sdk_deadline.types.integer
    import aws_sdk_deadline.types.min_zero_max_integer
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class FleetSummary(TypedDict):
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the fleet summary to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    status: "aws_sdk_deadline.types.fleet_status.FleetStatus"
    """<p>The status of the fleet.</p>"""
    status_message: NotRequired["aws_sdk_deadline.types.string.String"]
    """<p>A message that communicates a suspended status of the fleet.</p>"""
    auto_scaling_status: NotRequired[
        "aws_sdk_deadline.types.auto_scaling_status.AutoScalingStatus"
    ]
    """<p>The Auto Scaling status of a fleet.</p>"""
    target_worker_count: NotRequired["aws_sdk_deadline.types.integer.Integer"]
    """<p>The target number of workers in a fleet.</p>"""
    worker_count: "aws_sdk_deadline.types.integer.Integer"
    """<p>The number of workers in the fleet summary.</p>"""
    min_worker_count: "aws_sdk_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """<p>The minimum number of workers in the fleet.</p>"""
    max_worker_count: "aws_sdk_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """<p>The maximum number of workers specified in the fleet.</p>"""
    configuration: "aws_sdk_deadline.types.fleet_configuration.FleetConfiguration"
    """<p>The configuration details for the fleet.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetSummary) -> dict:
    out: dict = {}
    out["fleetId"] = value["fleet_id"]
    out["farmId"] = value["farm_id"]
    out["displayName"] = value["display_name"]
    import aws_sdk_deadline.types.fleet_status

    out["status"] = aws_sdk_deadline.types.fleet_status.serialize_json(value["status"])
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "auto_scaling_status" in value:
        import aws_sdk_deadline.types.auto_scaling_status

        out["autoScalingStatus"] = (
            aws_sdk_deadline.types.auto_scaling_status.serialize_json(
                value["auto_scaling_status"]
            )
        )
    if "target_worker_count" in value:
        out["targetWorkerCount"] = value["target_worker_count"]
    out["workerCount"] = value["worker_count"]
    out["minWorkerCount"] = value["min_worker_count"]
    out["maxWorkerCount"] = value["max_worker_count"]
    import aws_sdk_deadline.types.fleet_configuration

    out["configuration"] = aws_sdk_deadline.types.fleet_configuration.serialize_json(
        value["configuration"]
    )
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> FleetSummary:
    out: FleetSummary = {}  # type: ignore[typeddict-item]
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("FleetSummary.fleet_id required")
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("FleetSummary.farm_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("FleetSummary.display_name required")
    if "status" in data:
        import aws_sdk_deadline.types.fleet_status

        out["status"] = aws_sdk_deadline.types.fleet_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("FleetSummary.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "autoScalingStatus" in data:
        import aws_sdk_deadline.types.auto_scaling_status

        out["auto_scaling_status"] = (
            aws_sdk_deadline.types.auto_scaling_status.deserialize_json(
                data["autoScalingStatus"]
            )
        )
    if "targetWorkerCount" in data:
        out["target_worker_count"] = data["targetWorkerCount"]
    if "workerCount" in data:
        out["worker_count"] = data["workerCount"]
    else:
        raise DeserializationError("FleetSummary.worker_count required")
    if "minWorkerCount" in data:
        out["min_worker_count"] = data["minWorkerCount"]
    else:
        raise DeserializationError("FleetSummary.min_worker_count required")
    if "maxWorkerCount" in data:
        out["max_worker_count"] = data["maxWorkerCount"]
    else:
        raise DeserializationError("FleetSummary.max_worker_count required")
    if "configuration" in data:
        import aws_sdk_deadline.types.fleet_configuration

        out["configuration"] = (
            aws_sdk_deadline.types.fleet_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("FleetSummary.configuration required")
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("FleetSummary.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("FleetSummary.created_by required")
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
