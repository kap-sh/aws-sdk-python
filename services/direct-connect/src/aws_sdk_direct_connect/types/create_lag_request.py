"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateLagRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.bandwidth
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.count
    import aws_sdk_direct_connect.types.lag_name
    import aws_sdk_direct_connect.types.location_code
    import aws_sdk_direct_connect.types.provider_name
    import aws_sdk_direct_connect.types.request_mac_sec
    import aws_sdk_direct_connect.types.tag_list


class CreateLagRequest(TypedDict):
    number_of_connections: "aws_sdk_direct_connect.types.count.Count"
    """<p>The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1Gbps or 10Gbps, or two when the port speed is 100Gbps or 400Gbps.</p>"""
    location: "aws_sdk_direct_connect.types.location_code.LocationCode"
    """<p>The location for the LAG.</p>"""
    connections_bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth"
    """<p>The bandwidth of the individual physical dedicated connections bundled by the LAG. The possible values are 1Gbps,10Gbps, 100Gbps, and 400Gbps. </p>"""
    lag_name: "aws_sdk_direct_connect.types.lag_name.LagName"
    """<p>The name of the LAG.</p>"""
    connection_id: NotRequired[
        "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    ]
    """<p>The ID of an existing dedicated connection to migrate to the LAG.</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the LAG.</p>"""
    child_connection_tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the automtically created LAGs.</p>"""
    provider_name: NotRequired[
        "aws_sdk_direct_connect.types.provider_name.ProviderName"
    ]
    """<p>The name of the service provider associated with the LAG.</p>"""
    request_mac_sec: NotRequired[
        "aws_sdk_direct_connect.types.request_mac_sec.RequestMACSec"
    ]
    """<p>Indicates whether the connection will support MAC Security (MACsec).</p> <note> <p>All connections in the LAG must be capable of supporting MAC Security (MACsec). For information about MAC Security (MACsec) prerequisties, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-prerequisites\">MACsec prerequisties</a> in the <i>Direct Connect User Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLagRequest) -> dict:
    out: dict = {}
    out["numberOfConnections"] = value.get("number_of_connections", 0)
    out["location"] = value["location"]
    out["connectionsBandwidth"] = value["connections_bandwidth"]
    out["lagName"] = value["lag_name"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "tags" in value:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "child_connection_tags" in value:
        import aws_sdk_direct_connect.types.tag_list

        out["childConnectionTags"] = (
            aws_sdk_direct_connect.types.tag_list.serialize_aws_json_1_1(
                value["child_connection_tags"]
            )
        )
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "request_mac_sec" in value:
        out["requestMACSec"] = value["request_mac_sec"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLagRequest:
    out: CreateLagRequest = {}  # type: ignore[typeddict-item]
    if "numberOfConnections" in data:
        out["number_of_connections"] = data["numberOfConnections"]
    else:
        out["number_of_connections"] = 0
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError("CreateLagRequest.location required")
    if "connectionsBandwidth" in data:
        out["connections_bandwidth"] = data["connectionsBandwidth"]
    else:
        raise DeserializationError("CreateLagRequest.connections_bandwidth required")
    if "lagName" in data:
        out["lag_name"] = data["lagName"]
    else:
        raise DeserializationError("CreateLagRequest.lag_name required")
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    if "tags" in data:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "childConnectionTags" in data:
        import aws_sdk_direct_connect.types.tag_list

        out["child_connection_tags"] = (
            aws_sdk_direct_connect.types.tag_list.deserialize_aws_json_1_1(
                data["childConnectionTags"]
            )
        )
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    if "requestMACSec" in data:
        out["request_mac_sec"] = data["requestMACSec"]
    return out
