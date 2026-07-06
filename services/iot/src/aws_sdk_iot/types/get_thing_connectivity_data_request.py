"""Generated from Smithy shape ``com.amazonaws.iot#GetThingConnectivityDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.boolean
    import aws_sdk_iot.types.connectivity_api_thing_name


class GetThingConnectivityDataRequest(TypedDict, closed=True):
    thing_name: "aws_sdk_iot.types.connectivity_api_thing_name.ConnectivityApiThingName"
    """<p>The name of your IoT thing.</p>"""
    include_socket_information: NotRequired["aws_sdk_iot.types.boolean.Boolean"]
    """<p>Specifies if socket information (sourcePort, targetPort, sourceIp, targetIp, vpcEndpointId) should be included in the GetThingConnectivityData response. Set to <code>true</code> to include socket information. Set to <code>false</code> to omit socket information. By default, this is set to <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThingConnectivityDataRequest) -> dict:
    out: dict = {}
    if "include_socket_information" in value:
        out["includeSocketInformation"] = value["include_socket_information"]
    return out


def deserialize_json(data: dict) -> GetThingConnectivityDataRequest:
    out: GetThingConnectivityDataRequest = {}  # type: ignore[typeddict-item]
    if "includeSocketInformation" in data:
        out["include_socket_information"] = data["includeSocketInformation"]
    return out
