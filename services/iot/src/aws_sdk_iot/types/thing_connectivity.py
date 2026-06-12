"""Generated from Smithy shape ``com.amazonaws.iot#ThingConnectivity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.boolean
    import aws_sdk_iot.types.client_id
    import aws_sdk_iot.types.connectivity_timestamp
    import aws_sdk_iot.types.disconnect_reason
    import aws_sdk_iot.types.keep_alive_duration
    import aws_sdk_iot.types.session_expiry


class ThingConnectivity(TypedDict):
    connected: NotRequired["aws_sdk_iot.types.boolean.Boolean"]
    """<p>True if the thing is connected to the Amazon Web Services IoT Core service; false if it is not connected.</p>"""
    timestamp: NotRequired[
        "aws_sdk_iot.types.connectivity_timestamp.ConnectivityTimestamp"
    ]
    """<p>The epoch time (in milliseconds) when the thing last connected or disconnected.</p>"""
    disconnect_reason: NotRequired[
        "aws_sdk_iot.types.disconnect_reason.DisconnectReason"
    ]
    """<p>The reason that the client is disconnected.</p>"""
    keep_alive_duration: NotRequired[
        "aws_sdk_iot.types.keep_alive_duration.KeepAliveDuration"
    ]
    """<p>The keep-alive interval in seconds that the client specified when establishing the connection.</p>"""
    clean_session: NotRequired["aws_sdk_iot.types.boolean.Boolean"]
    """<p>Indicates whether the client is using a clean session. Returns <code>true</code> for clean sessions.</p>"""
    session_expiry: NotRequired["aws_sdk_iot.types.session_expiry.SessionExpiry"]
    """<p>The session expiry interval in seconds for the MQTT client connection. This value indicates how long the session will remain active after the client disconnects.</p>"""
    client_id: NotRequired["aws_sdk_iot.types.client_id.ClientId"]
    """<p>The unique identifier of the MQTT client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingConnectivity) -> dict:
    out: dict = {}
    if "connected" in value:
        out["connected"] = value["connected"]
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    if "disconnect_reason" in value:
        out["disconnectReason"] = value["disconnect_reason"]
    if "keep_alive_duration" in value:
        out["keepAliveDuration"] = value["keep_alive_duration"]
    if "clean_session" in value:
        out["cleanSession"] = value["clean_session"]
    if "session_expiry" in value:
        out["sessionExpiry"] = value["session_expiry"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> ThingConnectivity:
    out: ThingConnectivity = {}  # type: ignore[typeddict-item]
    if "connected" in data:
        out["connected"] = data["connected"]
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    if "disconnectReason" in data:
        out["disconnect_reason"] = data["disconnectReason"]
    if "keepAliveDuration" in data:
        out["keep_alive_duration"] = data["keepAliveDuration"]
    if "cleanSession" in data:
        out["clean_session"] = data["cleanSession"]
    if "sessionExpiry" in data:
        out["session_expiry"] = data["sessionExpiry"]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    return out
