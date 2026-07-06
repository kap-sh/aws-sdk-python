"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn_list
    import aws_sdk_mediaconnect.types.router_network_interface_arn_list
    import aws_sdk_mediaconnect.types.router_output_type_list
    import aws_sdk_mediaconnect.types.routing_scope_list
    import aws_sdk_mediaconnect.types.string_list


class _RouterOutputFilter_RegionNames(TypedDict, closed=True):
    RegionNames: "aws_sdk_mediaconnect.types.string_list.StringList"


class _RouterOutputFilter_NetworkInterfaceArns(TypedDict, closed=True):
    NetworkInterfaceArns: "aws_sdk_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList"


class _RouterOutputFilter_RoutingScopes(TypedDict, closed=True):
    RoutingScopes: "aws_sdk_mediaconnect.types.routing_scope_list.RoutingScopeList"


class _RouterOutputFilter_OutputTypes(TypedDict, closed=True):
    OutputTypes: (
        "aws_sdk_mediaconnect.types.router_output_type_list.RouterOutputTypeList"
    )


class _RouterOutputFilter_RoutedInputArns(TypedDict, closed=True):
    RoutedInputArns: (
        "aws_sdk_mediaconnect.types.router_input_arn_list.RouterInputArnList"
    )


class _RouterOutputFilter_NameContains(TypedDict, closed=True):
    NameContains: "aws_sdk_mediaconnect.types.string_list.StringList"


RouterOutputFilter: TypeAlias = (
    _RouterOutputFilter_RegionNames
    | _RouterOutputFilter_NetworkInterfaceArns
    | _RouterOutputFilter_RoutingScopes
    | _RouterOutputFilter_OutputTypes
    | _RouterOutputFilter_RoutedInputArns
    | _RouterOutputFilter_NameContains
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputFilter) -> dict:
    if "RegionNames" in value:
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
    elif "OutputTypes" in value:
        import aws_sdk_mediaconnect.types.router_output_type_list

        return {
            "outputTypes": aws_sdk_mediaconnect.types.router_output_type_list.serialize_json(
                value["OutputTypes"]
            )
        }
    elif "RoutedInputArns" in value:
        import aws_sdk_mediaconnect.types.router_input_arn_list

        return {
            "routedInputArns": aws_sdk_mediaconnect.types.router_input_arn_list.serialize_json(
                value["RoutedInputArns"]
            )
        }
    elif "NameContains" in value:
        import aws_sdk_mediaconnect.types.string_list

        return {
            "nameContains": aws_sdk_mediaconnect.types.string_list.serialize_json(
                value["NameContains"]
            )
        }
    else:
        raise SerializationError("RouterOutputFilter: no variant present")


def deserialize_json(data: dict) -> RouterOutputFilter:
    if "regionNames" in data:
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
    elif "outputTypes" in data:
        import aws_sdk_mediaconnect.types.router_output_type_list

        return {
            "OutputTypes": aws_sdk_mediaconnect.types.router_output_type_list.deserialize_json(
                data["outputTypes"]
            )
        }
    elif "routedInputArns" in data:
        import aws_sdk_mediaconnect.types.router_input_arn_list

        return {
            "RoutedInputArns": aws_sdk_mediaconnect.types.router_input_arn_list.deserialize_json(
                data["routedInputArns"]
            )
        }
    elif "nameContains" in data:
        import aws_sdk_mediaconnect.types.string_list

        return {
            "NameContains": aws_sdk_mediaconnect.types.string_list.deserialize_json(
                data["nameContains"]
            )
        }
    else:
        raise DeserializationError("RouterOutputFilter: no recognized variant key")
