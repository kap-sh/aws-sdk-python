"""Generated from Smithy shape ``com.amazonaws.opensearch#OutboundConnectionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.connection_status_message
    import aws_sdk_opensearch.types.outbound_connection_status_code


class OutboundConnectionStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "aws_sdk_opensearch.types.outbound_connection_status_code.OutboundConnectionStatusCode"
    ]
    """<p>The status code for the outbound connection. Can be one of the following:</p> <ul> <li> <p> <b>VALIDATING</b> - The outbound connection request is being validated.</p> </li> <li> <p> <b>VALIDATION_FAILED</b> - Validation failed for the connection request.</p> </li> <li> <p> <b>PENDING_ACCEPTANCE</b>: Outbound connection request is validated and is not yet accepted by the remote domain owner.</p> </li> <li> <p> <b>APPROVED</b> - Outbound connection has been approved by the remote domain owner for getting provisioned.</p> </li> <li> <p> <b>PROVISIONING</b> - Outbound connection request is in process.</p> </li> <li> <p> <b>ACTIVE</b> - Outbound connection is active and ready to use.</p> </li> <li> <p> <b>REJECTING</b> - Outbound connection rejection by remote domain owner is in progress.</p> </li> <li> <p> <b>REJECTED</b> - Outbound connection request is rejected by remote domain owner.</p> </li> <li> <p> <b>DELETING</b> - Outbound connection deletion is in progress.</p> </li> <li> <p> <b>DELETED</b> - Outbound connection is deleted and can no longer be used.</p> </li> </ul>"""
    message: NotRequired[
        "aws_sdk_opensearch.types.connection_status_message.ConnectionStatusMessage"
    ]
    """<p>Verbose information for the outbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundConnectionStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_opensearch.types.outbound_connection_status_code

        out["StatusCode"] = (
            aws_sdk_opensearch.types.outbound_connection_status_code.serialize_json(
                value["status_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> OutboundConnectionStatus:
    out: OutboundConnectionStatus = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import aws_sdk_opensearch.types.outbound_connection_status_code

        out["status_code"] = (
            aws_sdk_opensearch.types.outbound_connection_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
