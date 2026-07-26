"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.host_properties_request
    import capo_deadline.types.updated_worker_status
    import capo_deadline.types.worker_capabilities
    import capo_deadline.types.worker_id


class UpdateWorkerRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID to update.</p>"""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The worker ID to update.</p>"""
    status: NotRequired["capo_deadline.types.updated_worker_status.UpdatedWorkerStatus"]
    """<p>The worker status to update.</p>"""
    capabilities: NotRequired[
        "capo_deadline.types.worker_capabilities.WorkerCapabilities"
    ]
    """<p>The worker capabilities to update.</p>"""
    host_properties: NotRequired[
        "capo_deadline.types.host_properties_request.HostPropertiesRequest"
    ]
    """<p>The host properties to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkerRequest) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_deadline.types.updated_worker_status

        out["status"] = capo_deadline.types.updated_worker_status.serialize_json(
            value["status"]
        )
    if "capabilities" in value:
        import capo_deadline.types.worker_capabilities

        out["capabilities"] = capo_deadline.types.worker_capabilities.serialize_json(
            value["capabilities"]
        )
    if "host_properties" in value:
        import capo_deadline.types.host_properties_request

        out["hostProperties"] = (
            capo_deadline.types.host_properties_request.serialize_json(
                value["host_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkerRequest:
    out: UpdateWorkerRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_deadline.types.updated_worker_status

        out["status"] = capo_deadline.types.updated_worker_status.deserialize_json(
            data["status"]
        )
    if "capabilities" in data:
        import capo_deadline.types.worker_capabilities

        out["capabilities"] = capo_deadline.types.worker_capabilities.deserialize_json(
            data["capabilities"]
        )
    if "hostProperties" in data:
        import capo_deadline.types.host_properties_request

        out["host_properties"] = (
            capo_deadline.types.host_properties_request.deserialize_json(
                data["hostProperties"]
            )
        )
    return out
