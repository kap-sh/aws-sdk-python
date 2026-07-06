"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.bandwidth
    import aws_sdk_direct_connect.types.connection_name
    import aws_sdk_direct_connect.types.lag_id
    import aws_sdk_direct_connect.types.location_code
    import aws_sdk_direct_connect.types.provider_name
    import aws_sdk_direct_connect.types.request_mac_sec
    import aws_sdk_direct_connect.types.tag_list


class CreateConnectionRequest(TypedDict, closed=True):
    location: "aws_sdk_direct_connect.types.location_code.LocationCode"
    """<p>The location of the connection.</p>"""
    bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth"
    """<p>The bandwidth of the connection.</p>"""
    connection_name: "aws_sdk_direct_connect.types.connection_name.ConnectionName"
    """<p>The name of the connection.</p>"""
    lag_id: NotRequired["aws_sdk_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the lag.</p>"""
    provider_name: NotRequired[
        "aws_sdk_direct_connect.types.provider_name.ProviderName"
    ]
    """<p>The name of the service provider associated with the requested connection.</p>"""
    request_mac_sec: NotRequired[
        "aws_sdk_direct_connect.types.request_mac_sec.RequestMACSec"
    ]
    r"""<p>Indicates whether you want the connection to support MAC Security (MACsec).</p> <p>MAC Security (MACsec) is unavailable on hosted connections. For information about MAC Security (MACsec) prerequisites, see <a href=\"https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACSec.html\">MAC Security in Direct Connect</a> in the <i>Direct Connect User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    out["location"] = value["location"]
    out["bandwidth"] = value["bandwidth"]
    out["connectionName"] = value["connection_name"]
    if "lag_id" in value:
        out["lagId"] = value["lag_id"]
    if "tags" in value:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "request_mac_sec" in value:
        out["requestMACSec"] = value["request_mac_sec"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError("CreateConnectionRequest.location required")
    if "bandwidth" in data:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError("CreateConnectionRequest.bandwidth required")
    if "connectionName" in data:
        out["connection_name"] = data["connectionName"]
    else:
        raise DeserializationError("CreateConnectionRequest.connection_name required")
    if "lagId" in data:
        out["lag_id"] = data["lagId"]
    if "tags" in data:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    if "requestMACSec" in data:
        out["request_mac_sec"] = data["requestMACSec"]
    return out
