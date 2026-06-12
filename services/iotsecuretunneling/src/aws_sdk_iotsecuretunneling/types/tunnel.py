"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#Tunnel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.connection_state
    import aws_sdk_iotsecuretunneling.types.date_type
    import aws_sdk_iotsecuretunneling.types.description
    import aws_sdk_iotsecuretunneling.types.destination_config
    import aws_sdk_iotsecuretunneling.types.tag_list
    import aws_sdk_iotsecuretunneling.types.timeout_config
    import aws_sdk_iotsecuretunneling.types.tunnel_arn
    import aws_sdk_iotsecuretunneling.types.tunnel_id
    import aws_sdk_iotsecuretunneling.types.tunnel_status


class Tunnel(TypedDict):
    tunnel_id: NotRequired["aws_sdk_iotsecuretunneling.types.tunnel_id.TunnelId"]
    """<p>A unique alpha-numeric ID that identifies a tunnel.</p>"""
    tunnel_arn: NotRequired["aws_sdk_iotsecuretunneling.types.tunnel_arn.TunnelArn"]
    """<p>The Amazon Resource Name (ARN) of a tunnel.</p>"""
    status: NotRequired["aws_sdk_iotsecuretunneling.types.tunnel_status.TunnelStatus"]
    """<p>The status of a tunnel. Valid values are: Open and Closed.</p>"""
    source_connection_state: NotRequired[
        "aws_sdk_iotsecuretunneling.types.connection_state.ConnectionState"
    ]
    """<p>The connection state of the source application.</p>"""
    destination_connection_state: NotRequired[
        "aws_sdk_iotsecuretunneling.types.connection_state.ConnectionState"
    ]
    """<p>The connection state of the destination application.</p>"""
    description: NotRequired["aws_sdk_iotsecuretunneling.types.description.Description"]
    """<p>A description of the tunnel.</p>"""
    destination_config: NotRequired[
        "aws_sdk_iotsecuretunneling.types.destination_config.DestinationConfig"
    ]
    """<p>The destination configuration that specifies the thing name of the destination device and a service name that the local proxy uses to connect to the destination application.</p>"""
    timeout_config: NotRequired[
        "aws_sdk_iotsecuretunneling.types.timeout_config.TimeoutConfig"
    ]
    """<p>Timeout configuration for the tunnel.</p>"""
    tags: NotRequired["aws_sdk_iotsecuretunneling.types.tag_list.TagList"]
    """<p>A list of tag metadata associated with the secure tunnel.</p>"""
    created_at: NotRequired["aws_sdk_iotsecuretunneling.types.date_type.DateType"]
    """<p>The time when the tunnel was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_iotsecuretunneling.types.date_type.DateType"]
    """<p>The last time the tunnel was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tunnel) -> dict:
    out: dict = {}
    if "tunnel_id" in value:
        out["tunnelId"] = value["tunnel_id"]
    if "tunnel_arn" in value:
        out["tunnelArn"] = value["tunnel_arn"]
    if "status" in value:
        import aws_sdk_iotsecuretunneling.types.tunnel_status

        out["status"] = (
            aws_sdk_iotsecuretunneling.types.tunnel_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "source_connection_state" in value:
        import aws_sdk_iotsecuretunneling.types.connection_state

        out["sourceConnectionState"] = (
            aws_sdk_iotsecuretunneling.types.connection_state.serialize_aws_json_1_1(
                value["source_connection_state"]
            )
        )
    if "destination_connection_state" in value:
        import aws_sdk_iotsecuretunneling.types.connection_state

        out["destinationConnectionState"] = (
            aws_sdk_iotsecuretunneling.types.connection_state.serialize_aws_json_1_1(
                value["destination_connection_state"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "destination_config" in value:
        import aws_sdk_iotsecuretunneling.types.destination_config

        out["destinationConfig"] = (
            aws_sdk_iotsecuretunneling.types.destination_config.serialize_aws_json_1_1(
                value["destination_config"]
            )
        )
    if "timeout_config" in value:
        import aws_sdk_iotsecuretunneling.types.timeout_config

        out["timeoutConfig"] = (
            aws_sdk_iotsecuretunneling.types.timeout_config.serialize_aws_json_1_1(
                value["timeout_config"]
            )
        )
    if "tags" in value:
        import aws_sdk_iotsecuretunneling.types.tag_list

        out["tags"] = aws_sdk_iotsecuretunneling.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "created_at" in value:
        import aws_sdk_iotsecuretunneling.types.date_type

        out["createdAt"] = (
            aws_sdk_iotsecuretunneling.types.date_type.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_iotsecuretunneling.types.date_type

        out["lastUpdatedAt"] = (
            aws_sdk_iotsecuretunneling.types.date_type.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Tunnel:
    out: Tunnel = {}  # type: ignore[typeddict-item]
    if "tunnelId" in data:
        out["tunnel_id"] = data["tunnelId"]
    if "tunnelArn" in data:
        out["tunnel_arn"] = data["tunnelArn"]
    if "status" in data:
        import aws_sdk_iotsecuretunneling.types.tunnel_status

        out["status"] = (
            aws_sdk_iotsecuretunneling.types.tunnel_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "sourceConnectionState" in data:
        import aws_sdk_iotsecuretunneling.types.connection_state

        out["source_connection_state"] = (
            aws_sdk_iotsecuretunneling.types.connection_state.deserialize_aws_json_1_1(
                data["sourceConnectionState"]
            )
        )
    if "destinationConnectionState" in data:
        import aws_sdk_iotsecuretunneling.types.connection_state

        out["destination_connection_state"] = (
            aws_sdk_iotsecuretunneling.types.connection_state.deserialize_aws_json_1_1(
                data["destinationConnectionState"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "destinationConfig" in data:
        import aws_sdk_iotsecuretunneling.types.destination_config

        out["destination_config"] = (
            aws_sdk_iotsecuretunneling.types.destination_config.deserialize_aws_json_1_1(
                data["destinationConfig"]
            )
        )
    if "timeoutConfig" in data:
        import aws_sdk_iotsecuretunneling.types.timeout_config

        out["timeout_config"] = (
            aws_sdk_iotsecuretunneling.types.timeout_config.deserialize_aws_json_1_1(
                data["timeoutConfig"]
            )
        )
    if "tags" in data:
        import aws_sdk_iotsecuretunneling.types.tag_list

        out["tags"] = (
            aws_sdk_iotsecuretunneling.types.tag_list.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_iotsecuretunneling.types.date_type

        out["created_at"] = (
            aws_sdk_iotsecuretunneling.types.date_type.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_iotsecuretunneling.types.date_type

        out["last_updated_at"] = (
            aws_sdk_iotsecuretunneling.types.date_type.deserialize_aws_json_1_1(
                data["lastUpdatedAt"]
            )
        )
    return out
