"""Generated from Smithy shape ``com.amazonaws.opensearch#InboundConnectionStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.connection_status_message
    import aws_sdk_opensearch.types.inbound_connection_status_code


class InboundConnectionStatus(TypedDict):
    status_code: NotRequired[
        "aws_sdk_opensearch.types.inbound_connection_status_code.InboundConnectionStatusCode"
    ]
    """<p>The status code for the connection. Can be one of the following:</p> <ul> <li> <p> <b>PENDING_ACCEPTANCE</b> - Inbound connection is not yet accepted by the remote domain owner.</p> </li> <li> <p> <b>APPROVED</b>: Inbound connection is pending acceptance by the remote domain owner.</p> </li> <li> <p> <b>PROVISIONING</b>: Inbound connection is being provisioned.</p> </li> <li> <p> <b>ACTIVE</b>: Inbound connection is active and ready to use.</p> </li> <li> <p> <b>REJECTING</b>: Inbound connection rejection is in process.</p> </li> <li> <p> <b>REJECTED</b>: Inbound connection is rejected.</p> </li> <li> <p> <b>DELETING</b>: Inbound connection deletion is in progress.</p> </li> <li> <p> <b>DELETED</b>: Inbound connection is deleted and can no longer be used.</p> </li> </ul>"""
    message: NotRequired[
        "aws_sdk_opensearch.types.connection_status_message.ConnectionStatusMessage"
    ]
    """<p>Information about the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InboundConnectionStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_opensearch.types.inbound_connection_status_code

        out["StatusCode"] = (
            aws_sdk_opensearch.types.inbound_connection_status_code.serialize_json(
                value["status_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InboundConnectionStatus:
    out: InboundConnectionStatus = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import aws_sdk_opensearch.types.inbound_connection_status_code

        out["status_code"] = (
            aws_sdk_opensearch.types.inbound_connection_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
