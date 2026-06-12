"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#OutboundCrossClusterSearchConnectionStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_status_message
    import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection_status_code


class OutboundCrossClusterSearchConnectionStatus(TypedDict):
    status_code: NotRequired[
        "aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection_status_code.OutboundCrossClusterSearchConnectionStatusCode"
    ]
    """<p>The state code for outbound connection. This can be one of the following:</p> <ul> <li>VALIDATING: The outbound connection request is being validated.</li> <li>VALIDATION_FAILED: Validation failed for the connection request.</li> <li>PENDING_ACCEPTANCE: Outbound connection request is validated and is not yet accepted by destination domain owner.</li> <li>PROVISIONING: Outbound connection request is in process.</li> <li>ACTIVE: Outbound connection is active and ready to use.</li> <li>REJECTED: Outbound connection request is rejected by destination domain owner.</li> <li>DELETING: Outbound connection deletion is in progress.</li> <li>DELETED: Outbound connection is deleted and cannot be used further.</li> </ul>"""
    message: NotRequired[
        "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_status_message.CrossClusterSearchConnectionStatusMessage"
    ]
    """<p>Specifies verbose information for the outbound connection status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundCrossClusterSearchConnectionStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection_status_code

        out["StatusCode"] = (
            aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection_status_code.serialize_json(
                value["status_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> OutboundCrossClusterSearchConnectionStatus:
    out: OutboundCrossClusterSearchConnectionStatus = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection_status_code

        out["status_code"] = (
            aws_sdk_elasticsearch_service.types.outbound_cross_cluster_search_connection_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
