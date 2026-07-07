"""Generated from Smithy shape ``com.amazonaws.deadline#GetWorkerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.host_properties_response
    import aws_sdk_deadline.types.log_configuration
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by
    import aws_sdk_deadline.types.worker_id
    import aws_sdk_deadline.types.worker_status


class GetWorkerResponse(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""
    worker_id: "aws_sdk_deadline.types.worker_id.WorkerId"
    """<p>The worker ID.</p>"""
    host_properties: NotRequired[
        "aws_sdk_deadline.types.host_properties_response.HostPropertiesResponse"
    ]
    """<p>The host properties for the worker.</p>"""
    status: "aws_sdk_deadline.types.worker_status.WorkerStatus"
    """<p>The status of the worker.</p>"""
    log: NotRequired["aws_sdk_deadline.types.log_configuration.LogConfiguration"]
    """<p>The logs for the associated worker.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkerResponse) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    if "host_properties" in value:
        import aws_sdk_deadline.types.host_properties_response

        out["hostProperties"] = (
            aws_sdk_deadline.types.host_properties_response.serialize_json(
                value["host_properties"]
            )
        )
    import aws_sdk_deadline.types.worker_status

    out["status"] = aws_sdk_deadline.types.worker_status.serialize_json(value["status"])
    if "log" in value:
        import aws_sdk_deadline.types.log_configuration

        out["log"] = aws_sdk_deadline.types.log_configuration.serialize_json(
            value["log"]
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


def deserialize_json(data: dict) -> GetWorkerResponse:
    out: GetWorkerResponse = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("GetWorkerResponse.farm_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("GetWorkerResponse.fleet_id required")
    if "workerId" in data:
        out["worker_id"] = data["workerId"]
    else:
        raise DeserializationError("GetWorkerResponse.worker_id required")
    if "hostProperties" in data:
        import aws_sdk_deadline.types.host_properties_response

        out["host_properties"] = (
            aws_sdk_deadline.types.host_properties_response.deserialize_json(
                data["hostProperties"]
            )
        )
    if "status" in data:
        import aws_sdk_deadline.types.worker_status

        out["status"] = aws_sdk_deadline.types.worker_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetWorkerResponse.status required")
    if "log" in data:
        import aws_sdk_deadline.types.log_configuration

        out["log"] = aws_sdk_deadline.types.log_configuration.deserialize_json(
            data["log"]
        )
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetWorkerResponse.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetWorkerResponse.created_by required")
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
