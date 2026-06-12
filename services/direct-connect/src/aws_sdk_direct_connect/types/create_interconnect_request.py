"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateInterconnectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.bandwidth
    import aws_sdk_direct_connect.types.interconnect_name
    import aws_sdk_direct_connect.types.lag_id
    import aws_sdk_direct_connect.types.location_code
    import aws_sdk_direct_connect.types.provider_name
    import aws_sdk_direct_connect.types.request_mac_sec
    import aws_sdk_direct_connect.types.tag_list


class CreateInterconnectRequest(TypedDict):
    interconnect_name: "aws_sdk_direct_connect.types.interconnect_name.InterconnectName"
    """<p>The name of the interconnect.</p>"""
    bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth"
    """<p>The port bandwidth, in Gbps. The possible values are 1, 10, and 100.</p>"""
    location: "aws_sdk_direct_connect.types.location_code.LocationCode"
    """<p>The location of the interconnect.</p>"""
    lag_id: NotRequired["aws_sdk_direct_connect.types.lag_id.LagId"]
    """<p>The ID of the LAG.</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the interconnect.</p>"""
    provider_name: NotRequired[
        "aws_sdk_direct_connect.types.provider_name.ProviderName"
    ]
    """<p>The name of the service provider associated with the interconnect.</p>"""
    request_mac_sec: NotRequired[
        "aws_sdk_direct_connect.types.request_mac_sec.RequestMACSec"
    ]
    """<p>Indicates whether you want the interconnect to support MAC Security (MACsec).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInterconnectRequest) -> dict:
    out: dict = {}
    out["interconnectName"] = value["interconnect_name"]
    out["bandwidth"] = value["bandwidth"]
    out["location"] = value["location"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateInterconnectRequest:
    out: CreateInterconnectRequest = {}  # type: ignore[typeddict-item]
    if "interconnectName" in data:
        out["interconnect_name"] = data["interconnectName"]
    else:
        raise DeserializationError(
            "CreateInterconnectRequest.interconnect_name required"
        )
    if "bandwidth" in data:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError("CreateInterconnectRequest.bandwidth required")
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError("CreateInterconnectRequest.location required")
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
