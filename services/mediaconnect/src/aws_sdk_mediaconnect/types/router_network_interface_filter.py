"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface_type_list
    import aws_sdk_mediaconnect.types.string_list


class _RouterNetworkInterfaceFilter_RegionNames(TypedDict, closed=True):
    RegionNames: "aws_sdk_mediaconnect.types.string_list.StringList"


class _RouterNetworkInterfaceFilter_NetworkInterfaceTypes(TypedDict, closed=True):
    NetworkInterfaceTypes: "aws_sdk_mediaconnect.types.router_network_interface_type_list.RouterNetworkInterfaceTypeList"


class _RouterNetworkInterfaceFilter_NameContains(TypedDict, closed=True):
    NameContains: "aws_sdk_mediaconnect.types.string_list.StringList"


RouterNetworkInterfaceFilter: TypeAlias = (
    _RouterNetworkInterfaceFilter_RegionNames
    | _RouterNetworkInterfaceFilter_NetworkInterfaceTypes
    | _RouterNetworkInterfaceFilter_NameContains
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceFilter) -> dict:
    if "RegionNames" in value:
        import aws_sdk_mediaconnect.types.string_list

        return {
            "regionNames": aws_sdk_mediaconnect.types.string_list.serialize_json(
                value["RegionNames"]
            )
        }
    elif "NetworkInterfaceTypes" in value:
        import aws_sdk_mediaconnect.types.router_network_interface_type_list

        return {
            "networkInterfaceTypes": aws_sdk_mediaconnect.types.router_network_interface_type_list.serialize_json(
                value["NetworkInterfaceTypes"]
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
        raise SerializationError("RouterNetworkInterfaceFilter: no variant present")


def deserialize_json(data: dict) -> RouterNetworkInterfaceFilter:
    if "regionNames" in data:
        import aws_sdk_mediaconnect.types.string_list

        return {
            "RegionNames": aws_sdk_mediaconnect.types.string_list.deserialize_json(
                data["regionNames"]
            )
        }
    elif "networkInterfaceTypes" in data:
        import aws_sdk_mediaconnect.types.router_network_interface_type_list

        return {
            "NetworkInterfaceTypes": aws_sdk_mediaconnect.types.router_network_interface_type_list.deserialize_json(
                data["networkInterfaceTypes"]
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
        raise DeserializationError(
            "RouterNetworkInterfaceFilter: no recognized variant key"
        )
