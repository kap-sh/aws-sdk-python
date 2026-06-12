"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainMaintenanceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.maintenance_status
    import aws_sdk_opensearch.types.maintenance_status_message
    import aws_sdk_opensearch.types.maintenance_type
    import aws_sdk_opensearch.types.node_id
    import aws_sdk_opensearch.types.request_id
    import aws_sdk_opensearch.types.update_timestamp


class DomainMaintenanceDetails(TypedDict):
    maintenance_id: NotRequired["aws_sdk_opensearch.types.request_id.RequestId"]
    """<p>The ID of the requested action.</p>"""
    domain_name: NotRequired["aws_sdk_opensearch.types.domain_name.DomainName"]
    """<p>The name of the domain.</p>"""
    action: NotRequired["aws_sdk_opensearch.types.maintenance_type.MaintenanceType"]
    """<p>The name of the action.</p>"""
    node_id: NotRequired["aws_sdk_opensearch.types.node_id.NodeId"]
    """<p>The ID of the data node.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.maintenance_status.MaintenanceStatus"]
    """<p>The status of the action.</p>"""
    status_message: NotRequired[
        "aws_sdk_opensearch.types.maintenance_status_message.MaintenanceStatusMessage"
    ]
    """<p>The status message for the action.</p>"""
    created_at: NotRequired["aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time at which the action was created.</p>"""
    updated_at: NotRequired["aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time at which the action was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainMaintenanceDetails) -> dict:
    out: dict = {}
    if "maintenance_id" in value:
        out["MaintenanceId"] = value["maintenance_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "action" in value:
        import aws_sdk_opensearch.types.maintenance_type

        out["Action"] = aws_sdk_opensearch.types.maintenance_type.serialize_json(
            value["action"]
        )
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "status" in value:
        import aws_sdk_opensearch.types.maintenance_status

        out["Status"] = aws_sdk_opensearch.types.maintenance_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "created_at" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["CreatedAt"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_opensearch.types.update_timestamp

        out["UpdatedAt"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
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
        import aws_sdk_opensearch.types.maintenance_type

        out["action"] = aws_sdk_opensearch.types.maintenance_type.deserialize_json(
            data["Action"]
        )
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "Status" in data:
        import aws_sdk_opensearch.types.maintenance_status

        out["status"] = aws_sdk_opensearch.types.maintenance_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreatedAt" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["created_at"] = aws_sdk_opensearch.types.update_timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["updated_at"] = aws_sdk_opensearch.types.update_timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
