"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_type_list
    import aws_sdk_mediaconnect.types.router_network_interface_arn_list
    import aws_sdk_mediaconnect.types.routing_scope_list
    import aws_sdk_mediaconnect.types.string_list


class _RouterInputFilter_NameContains(TypedDict, closed=True):
    NameContains: "aws_sdk_mediaconnect.types.string_list.StringList"


class _RouterInputFilter_RegionNames(TypedDict, closed=True):
    RegionNames: "aws_sdk_mediaconnect.types.string_list.StringList"


class _RouterInputFilter_NetworkInterfaceArns(TypedDict, closed=True):
    NetworkInterfaceArns: "aws_sdk_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList"


class _RouterInputFilter_RoutingScopes(TypedDict, closed=True):
    RoutingScopes: "aws_sdk_mediaconnect.types.routing_scope_list.RoutingScopeList"


class _RouterInputFilter_InputTypes(TypedDict, closed=True):
    InputTypes: "aws_sdk_mediaconnect.types.router_input_type_list.RouterInputTypeList"


RouterInputFilter: TypeAlias = (
    _RouterInputFilter_NameContains
    | _RouterInputFilter_RegionNames
    | _RouterInputFilter_NetworkInterfaceArns
    | _RouterInputFilter_RoutingScopes
    | _RouterInputFilter_InputTypes
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputFilter) -> dict:
    if "NameContains" in value:
        import aws_sdk_mediaconnect.types.string_list

        return {
            "nameContains": aws_sdk_mediaconnect.types.string_list.serialize_json(
                value["NameContains"]
            )
        }
    elif "RegionNames" in value:
        import aws_sdk_mediaconnect.types.string_list

        return {
            "regionNames": aws_sdk_mediaconnect.types.string_list.serialize_json(
                value["RegionNames"]
            )
        }
    elif "NetworkInterfaceArns" in value:
        import aws_sdk_mediaconnect.types.router_network_interface_arn_list

        return {
            "networkInterfaceArns": aws_sdk_mediaconnect.types.router_network_interface_arn_list.serialize_json(
                value["NetworkInterfaceArns"]
            )
        }
    elif "RoutingScopes" in value:
        import aws_sdk_mediaconnect.types.routing_scope_list

        return {
            "routingScopes": aws_sdk_mediaconnect.types.routing_scope_list.serialize_json(
                value["RoutingScopes"]
            )
        }
    elif "InputTypes" in value:
        import aws_sdk_mediaconnect.types.router_input_type_list

        return {
            "inputTypes": aws_sdk_mediaconnect.types.router_input_type_list.serialize_json(
                value["InputTypes"]
            )
        }
    else:
        raise SerializationError("RouterInputFilter: no variant present")


def deserialize_json(data: dict) -> RouterInputFilter:
    if "nameContains" in data:
        import aws_sdk_mediaconnect.types.string_list

        return {
            "NameContains": aws_sdk_mediaconnect.types.string_list.deserialize_json(
                data["nameContains"]
            )
        }
    elif "regionNames" in data:
        import aws_sdk_mediaconnect.types.string_list

        return {
            "RegionNames": aws_sdk_mediaconnect.types.string_list.deserialize_json(
                data["regionNames"]
            )
        }
    elif "networkInterfaceArns" in data:
        import aws_sdk_mediaconnect.types.router_network_interface_arn_list

        return {
            "NetworkInterfaceArns": aws_sdk_mediaconnect.types.router_network_interface_arn_list.deserialize_json(
                data["networkInterfaceArns"]
            )
        }
    elif "routingScopes" in data:
        import aws_sdk_mediaconnect.types.routing_scope_list

        return {
            "RoutingScopes": aws_sdk_mediaconnect.types.routing_scope_list.deserialize_json(
                data["routingScopes"]
            )
        }
    elif "inputTypes" in data:
        import aws_sdk_mediaconnect.types.router_input_type_list

        return {
            "InputTypes": aws_sdk_mediaconnect.types.router_input_type_list.deserialize_json(
                data["inputTypes"]
            )
        }
    else:
        raise DeserializationError("RouterInputFilter: no recognized variant key")
