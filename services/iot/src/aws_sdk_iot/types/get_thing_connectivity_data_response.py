"""Generated from Smithy shape ``com.amazonaws.iot#GetThingConnectivityDataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.boolean
    import aws_sdk_iot.types.client_id
    import aws_sdk_iot.types.connectivity_api_thing_name
    import aws_sdk_iot.types.disconnect_reason_value
    import aws_sdk_iot.types.keep_alive_duration
    import aws_sdk_iot.types.session_expiry
    import aws_sdk_iot.types.source_ip
    import aws_sdk_iot.types.source_port
    import aws_sdk_iot.types.target_ip
    import aws_sdk_iot.types.target_port
    import aws_sdk_iot.types.timestamp
    import aws_sdk_iot.types.vpc_endpoint_id


class GetThingConnectivityDataResponse(TypedDict):
    thing_name: NotRequired[
        "aws_sdk_iot.types.connectivity_api_thing_name.ConnectivityApiThingName"
    ]
    """<p>The name of your IoT thing.</p>"""
    connected: NotRequired["aws_sdk_iot.types.boolean.Boolean"]
    """<p>A Boolean that indicates the connectivity status.</p>"""
    timestamp: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The timestamp of when the device connected or disconnected.</p>"""
    disconnect_reason: NotRequired[
        "aws_sdk_iot.types.disconnect_reason_value.DisconnectReasonValue"
    ]
    """<p>The reason that the client is disconnected.</p>"""
    source_ip: NotRequired["aws_sdk_iot.types.source_ip.SourceIp"]
    """<p>The IP address of the client that initiated the connection.</p>"""
    source_port: NotRequired["aws_sdk_iot.types.source_port.SourcePort"]
    """<p>The client's source port.</p>"""
    target_ip: NotRequired["aws_sdk_iot.types.target_ip.TargetIp"]
    """<p>The IP address of the Amazon Web Services IoT Core endpoint that the client connected to.</p>"""
    target_port: NotRequired["aws_sdk_iot.types.target_port.TargetPort"]
    """<p>The port number of the Amazon Web Services IoT Core endpoint that the client connected to.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_iot.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the VPC endpoint. Present for clients connected to Amazon Web Services IoT Core via a VPC endpoint.</p>"""
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
def serialize_json(value: GetThingConnectivityDataResponse) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "connected" in value:
        out["connected"] = value["connected"]
    if "timestamp" in value:
        import aws_sdk_iot.types.timestamp

        out["timestamp"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "disconnect_reason" in value:
        import aws_sdk_iot.types.disconnect_reason_value

        out["disconnectReason"] = (
            aws_sdk_iot.types.disconnect_reason_value.serialize_json(
                value["disconnect_reason"]
            )
        )
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    if "source_port" in value:
        out["sourcePort"] = value["source_port"]
    if "target_ip" in value:
        out["targetIp"] = value["target_ip"]
    if "target_port" in value:
        out["targetPort"] = value["target_port"]
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    if "keep_alive_duration" in value:
        out["keepAliveDuration"] = value["keep_alive_duration"]
    if "clean_session" in value:
        out["cleanSession"] = value["clean_session"]
    if "session_expiry" in value:
        out["sessionExpiry"] = value["session_expiry"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> GetThingConnectivityDataResponse:
    out: GetThingConnectivityDataResponse = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "connected" in data:
        out["connected"] = data["connected"]
    if "timestamp" in data:
        import aws_sdk_iot.types.timestamp

        out["timestamp"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["timestamp"]
        )
    if "disconnectReason" in data:
        import aws_sdk_iot.types.disconnect_reason_value

        out["disconnect_reason"] = (
            aws_sdk_iot.types.disconnect_reason_value.deserialize_json(
                data["disconnectReason"]
            )
        )
    if "sourceIp" in data:
        out["source_ip"] = data["sourceIp"]
    if "sourcePort" in data:
        out["source_port"] = data["sourcePort"]
    if "targetIp" in data:
        out["target_ip"] = data["targetIp"]
    if "targetPort" in data:
        out["target_port"] = data["targetPort"]
    if "vpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    if "keepAliveDuration" in data:
        out["keep_alive_duration"] = data["keepAliveDuration"]
    if "cleanSession" in data:
        out["clean_session"] = data["cleanSession"]
    if "sessionExpiry" in data:
        out["session_expiry"] = data["sessionExpiry"]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    return out
