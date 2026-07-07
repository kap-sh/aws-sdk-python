"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.host_properties_response
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by
    import aws_sdk_deadline.types.worker_id
    import aws_sdk_deadline.types.worker_status


class WorkerSearchSummary(TypedDict, closed=True):
    fleet_id: NotRequired["aws_sdk_deadline.types.fleet_id.FleetId"]
    """<p>The fleet ID.</p>"""
    worker_id: NotRequired["aws_sdk_deadline.types.worker_id.WorkerId"]
    """<p>The worker ID.</p>"""
    status: NotRequired["aws_sdk_deadline.types.worker_status.WorkerStatus"]
    """<p>The status of the worker search.</p>"""
    host_properties: NotRequired[
        "aws_sdk_deadline.types.host_properties_response.HostPropertiesResponse"
    ]
    """<p>Provides the Amazon EC2 instance properties of the worker host.</p>"""
    created_by: NotRequired["aws_sdk_deadline.types.created_by.CreatedBy"]
    """<p>The user or system that created this resource.</p>"""
    created_at: NotRequired["aws_sdk_deadline.types.created_at.CreatedAt"]
    """<p>The date and time the resource was created.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerSearchSummary) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["fleetId"] = value["fleet_id"]
    if "worker_id" in value:
        out["workerId"] = value["worker_id"]
    if "status" in value:
        import aws_sdk_deadline.types.worker_status

        out["status"] = aws_sdk_deadline.types.worker_status.serialize_json(
            value["status"]
        )
    if "host_properties" in value:
        import aws_sdk_deadline.types.host_properties_response

        out["hostProperties"] = (
            aws_sdk_deadline.types.host_properties_response.serialize_json(
                value["host_properties"]
            )
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import aws_sdk_deadline.types.created_at

        out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
            value["created_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> WorkerSearchSummary:
    out: WorkerSearchSummary = {}  # type: ignore[typeddict-item]
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    if "workerId" in data:
        out["worker_id"] = data["workerId"]
    if "status" in data:
        import aws_sdk_deadline.types.worker_status

        out["status"] = aws_sdk_deadline.types.worker_status.deserialize_json(
            data["status"]
        )
    if "hostProperties" in data:
        import aws_sdk_deadline.types.host_properties_response

        out["host_properties"] = (
            aws_sdk_deadline.types.host_properties_response.deserialize_json(
                data["hostProperties"]
            )
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    return out
