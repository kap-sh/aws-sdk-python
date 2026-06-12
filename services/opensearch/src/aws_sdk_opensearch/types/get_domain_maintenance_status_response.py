"""Generated from Smithy shape ``com.amazonaws.opensearch#GetDomainMaintenanceStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.maintenance_status
    import aws_sdk_opensearch.types.maintenance_status_message
    import aws_sdk_opensearch.types.maintenance_type
    import aws_sdk_opensearch.types.node_id
    import aws_sdk_opensearch.types.update_timestamp


class GetDomainMaintenanceStatusResponse(TypedDict):
    status: NotRequired["aws_sdk_opensearch.types.maintenance_status.MaintenanceStatus"]
    """<p>The status of the maintenance action.</p>"""
    status_message: NotRequired[
        "aws_sdk_opensearch.types.maintenance_status_message.MaintenanceStatusMessage"
    ]
    """<p>The status message of the maintenance action.</p>"""
    node_id: NotRequired["aws_sdk_opensearch.types.node_id.NodeId"]
    """<p>The node ID of the maintenance action.</p>"""
    action: NotRequired["aws_sdk_opensearch.types.maintenance_type.MaintenanceType"]
    """<p>The action name.</p>"""
    created_at: NotRequired["aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time at which the action was created.</p>"""
    updated_at: NotRequired["aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time at which the action was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainMaintenanceStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_opensearch.types.maintenance_status

        out["Status"] = aws_sdk_opensearch.types.maintenance_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "action" in value:
        import aws_sdk_opensearch.types.maintenance_type

        out["Action"] = aws_sdk_opensearch.types.maintenance_type.serialize_json(
            value["action"]
        )
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


def deserialize_json(data: dict) -> GetDomainMaintenanceStatusResponse:
    out: GetDomainMaintenanceStatusResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_opensearch.types.maintenance_status

        out["status"] = aws_sdk_opensearch.types.maintenance_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "Action" in data:
        import aws_sdk_opensearch.types.maintenance_type

        out["action"] = aws_sdk_opensearch.types.maintenance_type.deserialize_json(
            data["Action"]
        )
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
