"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#Tunnel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.connection_state
    import capo_iotsecuretunneling.types.date_type
    import capo_iotsecuretunneling.types.description
    import capo_iotsecuretunneling.types.destination_config
    import capo_iotsecuretunneling.types.tag_list
    import capo_iotsecuretunneling.types.timeout_config
    import capo_iotsecuretunneling.types.tunnel_arn
    import capo_iotsecuretunneling.types.tunnel_id
    import capo_iotsecuretunneling.types.tunnel_status


class Tunnel(TypedDict, closed=True):
    tunnel_id: NotRequired["capo_iotsecuretunneling.types.tunnel_id.TunnelId"]
    """<p>A unique alpha-numeric ID that identifies a tunnel.</p>"""
    tunnel_arn: NotRequired["capo_iotsecuretunneling.types.tunnel_arn.TunnelArn"]
    """<p>The Amazon Resource Name (ARN) of a tunnel.</p>"""
    status: NotRequired["capo_iotsecuretunneling.types.tunnel_status.TunnelStatus"]
    """<p>The status of a tunnel. Valid values are: Open and Closed.</p>"""
    source_connection_state: NotRequired[
        "capo_iotsecuretunneling.types.connection_state.ConnectionState"
    ]
    """<p>The connection state of the source application.</p>"""
    destination_connection_state: NotRequired[
        "capo_iotsecuretunneling.types.connection_state.ConnectionState"
    ]
    """<p>The connection state of the destination application.</p>"""
    description: NotRequired["capo_iotsecuretunneling.types.description.Description"]
    """<p>A description of the tunnel.</p>"""
    destination_config: NotRequired[
        "capo_iotsecuretunneling.types.destination_config.DestinationConfig"
    ]
    """<p>The destination configuration that specifies the thing name of the destination device and a service name that the local proxy uses to connect to the destination application.</p>"""
    timeout_config: NotRequired[
        "capo_iotsecuretunneling.types.timeout_config.TimeoutConfig"
    ]
    """<p>Timeout configuration for the tunnel.</p>"""
    tags: NotRequired["capo_iotsecuretunneling.types.tag_list.TagList"]
    """<p>A list of tag metadata associated with the secure tunnel.</p>"""
    created_at: NotRequired["capo_iotsecuretunneling.types.date_type.DateType"]
    """<p>The time when the tunnel was created.</p>"""
    last_updated_at: NotRequired["capo_iotsecuretunneling.types.date_type.DateType"]
    """<p>The last time the tunnel was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tunnel) -> dict:
    out: dict = {}
    if "tunnel_id" in value:
        out["tunnelId"] = value["tunnel_id"]
    if "tunnel_arn" in value:
        out["tunnelArn"] = value["tunnel_arn"]
    if "status" in value:
        import capo_iotsecuretunneling.types.tunnel_status

        out["status"] = (
            capo_iotsecuretunneling.types.tunnel_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "source_connection_state" in value:
        import capo_iotsecuretunneling.types.connection_state

        out["sourceConnectionState"] = (
            capo_iotsecuretunneling.types.connection_state.serialize_aws_json_1_1(
                value["source_connection_state"]
            )
        )
    if "destination_connection_state" in value:
        import capo_iotsecuretunneling.types.connection_state

        out["destinationConnectionState"] = (
            capo_iotsecuretunneling.types.connection_state.serialize_aws_json_1_1(
                value["destination_connection_state"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "destination_config" in value:
        import capo_iotsecuretunneling.types.destination_config

        out["destinationConfig"] = (
            capo_iotsecuretunneling.types.destination_config.serialize_aws_json_1_1(
                value["destination_config"]
            )
        )
    if "timeout_config" in value:
        import capo_iotsecuretunneling.types.timeout_config

        out["timeoutConfig"] = (
            capo_iotsecuretunneling.types.timeout_config.serialize_aws_json_1_1(
                value["timeout_config"]
            )
        )
    if "tags" in value:
        import capo_iotsecuretunneling.types.tag_list

        out["tags"] = capo_iotsecuretunneling.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "created_at" in value:
        import capo_iotsecuretunneling.types.date_type

        out["createdAt"] = (
            capo_iotsecuretunneling.types.date_type.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_iotsecuretunneling.types.date_type

        out["lastUpdatedAt"] = (
            capo_iotsecuretunneling.types.date_type.serialize_aws_json_1_1(
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
        import capo_iotsecuretunneling.types.tunnel_status

        out["status"] = (
            capo_iotsecuretunneling.types.tunnel_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "sourceConnectionState" in data:
        import capo_iotsecuretunneling.types.connection_state

        out["source_connection_state"] = (
            capo_iotsecuretunneling.types.connection_state.deserialize_aws_json_1_1(
                data["sourceConnectionState"]
            )
        )
    if "destinationConnectionState" in data:
        import capo_iotsecuretunneling.types.connection_state

        out["destination_connection_state"] = (
            capo_iotsecuretunneling.types.connection_state.deserialize_aws_json_1_1(
                data["destinationConnectionState"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "destinationConfig" in data:
        import capo_iotsecuretunneling.types.destination_config

        out["destination_config"] = (
            capo_iotsecuretunneling.types.destination_config.deserialize_aws_json_1_1(
                data["destinationConfig"]
            )
        )
    if "timeoutConfig" in data:
        import capo_iotsecuretunneling.types.timeout_config

        out["timeout_config"] = (
            capo_iotsecuretunneling.types.timeout_config.deserialize_aws_json_1_1(
                data["timeoutConfig"]
            )
        )
    if "tags" in data:
        import capo_iotsecuretunneling.types.tag_list

        out["tags"] = capo_iotsecuretunneling.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "createdAt" in data:
        import capo_iotsecuretunneling.types.date_type

        out["created_at"] = (
            capo_iotsecuretunneling.types.date_type.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import capo_iotsecuretunneling.types.date_type

        out["last_updated_at"] = (
            capo_iotsecuretunneling.types.date_type.deserialize_aws_json_1_1(
                data["lastUpdatedAt"]
            )
        )
    return out
