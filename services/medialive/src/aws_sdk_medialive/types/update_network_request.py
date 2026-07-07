"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_ip_pool_update_request
    import aws_sdk_medialive.types.__list_of_route_update_request
    import aws_sdk_medialive.types.__string


class UpdateNetworkRequest(TypedDict, closed=True):
    ip_pools: NotRequired[
        "aws_sdk_medialive.types.__list_of_ip_pool_update_request.__listOfIpPoolUpdateRequest"
    ]
    """Include this parameter only if you want to change the pool of IP addresses in the network. An array of IpPoolCreateRequests that identify a collection of IP addresses in this network that you want to reserve for use in MediaLive Anywhere. MediaLive Anywhere uses these IP addresses for Push inputs (in both Bridge and NAT networks) and for output destinations (only in Bridge networks). Each IpPoolUpdateRequest specifies one CIDR block."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Include this parameter only if you want to change the name of the Network. Specify a name that is unique in the AWS account. Names are case-sensitive."""
    network_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the network"""
    routes: NotRequired[
        "aws_sdk_medialive.types.__list_of_route_update_request.__listOfRouteUpdateRequest"
    ]
    """Include this parameter only if you want to change or add routes in the Network. An array of Routes that MediaLive Anywhere needs to know about in order to route encoding traffic."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkRequest) -> dict:
    out: dict = {}
    if "ip_pools" in value:
        import aws_sdk_medialive.types.__list_of_ip_pool_update_request

        out["ipPools"] = (
            aws_sdk_medialive.types.__list_of_ip_pool_update_request.serialize_json(
                value["ip_pools"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "routes" in value:
        import aws_sdk_medialive.types.__list_of_route_update_request

        out["routes"] = (
            aws_sdk_medialive.types.__list_of_route_update_request.serialize_json(
                value["routes"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateNetworkRequest:
    out: UpdateNetworkRequest = {}  # type: ignore[typeddict-item]
    if "ipPools" in data:
        import aws_sdk_medialive.types.__list_of_ip_pool_update_request

        out["ip_pools"] = (
            aws_sdk_medialive.types.__list_of_ip_pool_update_request.deserialize_json(
                data["ipPools"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "routes" in data:
        import aws_sdk_medialive.types.__list_of_route_update_request

        out["routes"] = (
            aws_sdk_medialive.types.__list_of_route_update_request.deserialize_json(
                data["routes"]
            )
        )
    return out
