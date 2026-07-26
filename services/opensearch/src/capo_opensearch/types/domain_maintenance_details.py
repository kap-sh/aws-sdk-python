"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainMaintenanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.maintenance_status
    import capo_opensearch.types.maintenance_status_message
    import capo_opensearch.types.maintenance_type
    import capo_opensearch.types.node_id
    import capo_opensearch.types.request_id
    import capo_opensearch.types.update_timestamp


class DomainMaintenanceDetails(TypedDict, closed=True):
    maintenance_id: NotRequired["capo_opensearch.types.request_id.RequestId"]
    """<p>The ID of the requested action.</p>"""
    domain_name: NotRequired["capo_opensearch.types.domain_name.DomainName"]
    """<p>The name of the domain.</p>"""
    action: NotRequired["capo_opensearch.types.maintenance_type.MaintenanceType"]
    """<p>The name of the action.</p>"""
    node_id: NotRequired["capo_opensearch.types.node_id.NodeId"]
    """<p>The ID of the data node.</p>"""
    status: NotRequired["capo_opensearch.types.maintenance_status.MaintenanceStatus"]
    """<p>The status of the action.</p>"""
    status_message: NotRequired[
        "capo_opensearch.types.maintenance_status_message.MaintenanceStatusMessage"
    ]
    """<p>The status message for the action.</p>"""
    created_at: NotRequired["capo_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time at which the action was created.</p>"""
    updated_at: NotRequired["capo_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time at which the action was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainMaintenanceDetails) -> dict:
    out: dict = {}
    if "maintenance_id" in value:
        out["MaintenanceId"] = value["maintenance_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "action" in value:
        import capo_opensearch.types.maintenance_type

        out["Action"] = capo_opensearch.types.maintenance_type.serialize_json(
            value["action"]
        )
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "status" in value:
        import capo_opensearch.types.maintenance_status

        out["Status"] = capo_opensearch.types.maintenance_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "created_at" in value:
        import capo_opensearch.types.update_timestamp

        out["CreatedAt"] = capo_opensearch.types.update_timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_opensearch.types.update_timestamp

        out["UpdatedAt"] = capo_opensearch.types.update_timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> DomainMaintenanceDetails:
    out: DomainMaintenanceDetails = {}  # type: ignore[typeddict-item]
    if "MaintenanceId" in data:
        out["maintenance_id"] = data["MaintenanceId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "Action" in data:
        import capo_opensearch.types.maintenance_type

        out["action"] = capo_opensearch.types.maintenance_type.deserialize_json(
            data["Action"]
        )
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "Status" in data:
        import capo_opensearch.types.maintenance_status

        out["status"] = capo_opensearch.types.maintenance_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreatedAt" in data:
        import capo_opensearch.types.update_timestamp

        out["created_at"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_opensearch.types.update_timestamp

        out["updated_at"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
