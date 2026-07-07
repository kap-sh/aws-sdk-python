"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#InboundCrossClusterSearchConnectionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_status_message
    import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection_status_code


class InboundCrossClusterSearchConnectionStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection_status_code.InboundCrossClusterSearchConnectionStatusCode"
    ]
    """<p>The state code for inbound connection. This can be one of the following:</p> <ul> <li>PENDING_ACCEPTANCE: Inbound connection is not yet accepted by destination domain owner.</li> <li>APPROVED: Inbound connection is pending acceptance by destination domain owner.</li> <li>REJECTING: Inbound connection rejection is in process.</li> <li>REJECTED: Inbound connection is rejected.</li> <li>DELETING: Inbound connection deletion is in progress.</li> <li>DELETED: Inbound connection is deleted and cannot be used further.</li> </ul>"""
    message: NotRequired[
        "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_status_message.CrossClusterSearchConnectionStatusMessage"
    ]
    """<p>Specifies verbose information for the inbound connection status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InboundCrossClusterSearchConnectionStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection_status_code

        out["StatusCode"] = (
            aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection_status_code.serialize_json(
                value["status_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InboundCrossClusterSearchConnectionStatus:
    out: InboundCrossClusterSearchConnectionStatus = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection_status_code

        out["status_code"] = (
            aws_sdk_elasticsearch_service.types.inbound_cross_cluster_search_connection_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
