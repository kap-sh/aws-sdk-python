"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateRouterNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.router_network_interface_configuration


class CreateRouterNetworkInterfaceRequest(TypedDict):
    name: "str"
    """<p>The name of the router network interface.</p>"""
    configuration: "aws_sdk_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
    """<p>The configuration settings for the router network interface.</p>"""
    region_name: NotRequired["str"]
    """<p>The Amazon Web Services Region for the router network interface. Defaults to the current region if not specified.</p>"""
    tags: NotRequired["aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p>Key-value pairs that can be used to tag and organize this router network interface.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique identifier for the request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouterNetworkInterfaceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_mediaconnect.types.router_network_interface_configuration

    out["configuration"] = (
        aws_sdk_mediaconnect.types.router_network_interface_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "region_name" in value:
        out["regionName"] = value["region_name"]
    if "tags" in value:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["tags"] = aws_sdk_mediaconnect.types.__map_of_string.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRouterNetworkInterfaceRequest:
    out: CreateRouterNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRouterNetworkInterfaceRequest.name required")
    if "configuration" in data:
        import aws_sdk_mediaconnect.types.router_network_interface_configuration

        out["configuration"] = (
            aws_sdk_mediaconnect.types.router_network_interface_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRouterNetworkInterfaceRequest.configuration required"
        )
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    if "tags" in data:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["tags"] = aws_sdk_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
