"""Generated from Smithy shape ``com.amazonaws.medialive#CreateNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_ip_pool_create_request
    import capo_medialive.types.__list_of_route_create_request
    import capo_medialive.types.__string
    import capo_medialive.types.tags


class CreateNetworkRequest(TypedDict, closed=True):
    ip_pools: NotRequired[
        "capo_medialive.types.__list_of_ip_pool_create_request.__listOfIpPoolCreateRequest"
    ]
    """An array of IpPoolCreateRequests that identify a collection of IP addresses in your network that you want to reserve for use in MediaLive Anywhere. MediaLiveAnywhere uses these IP addresses for Push inputs (in both Bridge and NATnetworks) and for output destinations (only in Bridge networks). EachIpPoolUpdateRequest specifies one CIDR block."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """Specify a name that is unique in the AWS account. We recommend that you assign a name that hints at the type of traffic on the network. Names are case-sensitive."""
    request_id: NotRequired["capo_medialive.types.__string.__string"]
    """An ID that you assign to a create request. This ID ensures idempotency when creating resources."""
    routes: NotRequired[
        "capo_medialive.types.__list_of_route_create_request.__listOfRouteCreateRequest"
    ]
    """An array of routes that MediaLive Anywhere needs to know about in order to route encoding traffic."""
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkRequest) -> dict:
    out: dict = {}
    if "ip_pools" in value:
        import capo_medialive.types.__list_of_ip_pool_create_request

        out["ipPools"] = (
            capo_medialive.types.__list_of_ip_pool_create_request.serialize_json(
                value["ip_pools"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "routes" in value:
        import capo_medialive.types.__list_of_route_create_request

        out["routes"] = (
            capo_medialive.types.__list_of_route_create_request.serialize_json(
                value["routes"]
            )
        )
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateNetworkRequest:
    out: CreateNetworkRequest = {}  # type: ignore[typeddict-item]
    if "ipPools" in data:
        import capo_medialive.types.__list_of_ip_pool_create_request

        out["ip_pools"] = (
            capo_medialive.types.__list_of_ip_pool_create_request.deserialize_json(
                data["ipPools"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "routes" in data:
        import capo_medialive.types.__list_of_route_create_request

        out["routes"] = (
            capo_medialive.types.__list_of_route_create_request.deserialize_json(
                data["routes"]
            )
        )
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    return out
