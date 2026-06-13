"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterface``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.router_network_interface_arn
    import aws_sdk_mediaconnect.types.router_network_interface_configuration
    import aws_sdk_mediaconnect.types.router_network_interface_state
    import aws_sdk_mediaconnect.types.router_network_interface_type


class RouterNetworkInterface(TypedDict):
    name: "str"
    """<p>The name of the router network interface.</p>"""
    arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    """<p>The Amazon Resource Name (ARN) of the router network interface.</p>"""
    id: "str"
    """<p>The unique identifier of the router network interface.</p>"""
    state: "aws_sdk_mediaconnect.types.router_network_interface_state.RouterNetworkInterfaceState"
    """<p>The current state of the router network interface.</p>"""
    network_interface_type: "aws_sdk_mediaconnect.types.router_network_interface_type.RouterNetworkInterfaceType"
    """<p>The type of the router network interface.</p>"""
    configuration: "aws_sdk_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
    associated_output_count: "int"
    """<p>The number of router outputs associated with the network interface.</p>"""
    associated_input_count: "int"
    """<p>The number of router inputs associated with the network interface.</p>"""
    region_name: "str"
    """<p>The Amazon Web Services Region where the router network interface is located.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the router network interface was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router network interface was last updated.</p>"""
    tags: "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
    """<p>Key-value pairs that can be used to tag and organize this router network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterface) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import aws_sdk_mediaconnect.types.router_network_interface_state

    out["state"] = (
        aws_sdk_mediaconnect.types.router_network_interface_state.serialize_json(
            value["state"]
        )
    )
    import aws_sdk_mediaconnect.types.router_network_interface_type

    out["networkInterfaceType"] = (
        aws_sdk_mediaconnect.types.router_network_interface_type.serialize_json(
            value["network_interface_type"]
        )
    )
    import aws_sdk_mediaconnect.types.router_network_interface_configuration

    out["configuration"] = (
        aws_sdk_mediaconnect.types.router_network_interface_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["associatedOutputCount"] = value["associated_output_count"]
    out["associatedInputCount"] = value["associated_input_count"]
    out["regionName"] = value["region_name"]
    import aws_sdk_mediaconnect.types._prelude.timestamp

    out["createdAt"] = aws_sdk_mediaconnect.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_mediaconnect.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_mediaconnect.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    import aws_sdk_mediaconnect.types.__map_of_string

    out["tags"] = aws_sdk_mediaconnect.types.__map_of_string.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> RouterNetworkInterface:
    out: RouterNetworkInterface = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RouterNetworkInterface.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RouterNetworkInterface.arn required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("RouterNetworkInterface.id required")
    if "state" in data:
        import aws_sdk_mediaconnect.types.router_network_interface_state

        out["state"] = (
            aws_sdk_mediaconnect.types.router_network_interface_state.deserialize_json(
                data["state"]
            )
        )
    else:
        raise DeserializationError("RouterNetworkInterface.state required")
    if "networkInterfaceType" in data:
        import aws_sdk_mediaconnect.types.router_network_interface_type

        out["network_interface_type"] = (
            aws_sdk_mediaconnect.types.router_network_interface_type.deserialize_json(
                data["networkInterfaceType"]
            )
        )
    else:
        raise DeserializationError(
            "RouterNetworkInterface.network_interface_type required"
        )
    if "configuration" in data:
        import aws_sdk_mediaconnect.types.router_network_interface_configuration

        out["configuration"] = (
            aws_sdk_mediaconnect.types.router_network_interface_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("RouterNetworkInterface.configuration required")
    if "associatedOutputCount" in data:
        out["associated_output_count"] = data["associatedOutputCount"]
    else:
        raise DeserializationError(
            "RouterNetworkInterface.associated_output_count required"
        )
    if "associatedInputCount" in data:
        out["associated_input_count"] = data["associatedInputCount"]
    else:
        raise DeserializationError(
            "RouterNetworkInterface.associated_input_count required"
        )
    if "regionName" in data:
        out["region_name"] = data["regionName"]
    else:
        raise DeserializationError("RouterNetworkInterface.region_name required")
    if "createdAt" in data:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_mediaconnect.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("RouterNetworkInterface.created_at required")
    if "updatedAt" in data:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_mediaconnect.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("RouterNetworkInterface.updated_at required")
    if "tags" in data:
        import aws_sdk_mediaconnect.types.__map_of_string

        out["tags"] = aws_sdk_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("RouterNetworkInterface.tags required")
    return out
