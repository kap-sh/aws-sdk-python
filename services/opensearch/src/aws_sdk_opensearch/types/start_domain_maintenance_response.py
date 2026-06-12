"""Generated from Smithy shape ``com.amazonaws.opensearch#StartDomainMaintenanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.request_id


class StartDomainMaintenanceResponse(TypedDict):
    maintenance_id: NotRequired["aws_sdk_opensearch.types.request_id.RequestId"]
    """<p>The request ID of requested action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDomainMaintenanceResponse) -> dict:
    out: dict = {}
    if "maintenance_id" in value:
        out["MaintenanceId"] = value["maintenance_id"]
    return out


def deserialize_json(data: dict) -> StartDomainMaintenanceResponse:
    out: StartDomainMaintenanceResponse = {}  # type: ignore[typeddict-item]
    if "MaintenanceId" in data:
        out["maintenance_id"] = data["MaintenanceId"]
    return out
