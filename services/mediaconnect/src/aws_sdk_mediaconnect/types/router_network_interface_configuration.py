"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.public_router_network_interface_configuration
    import aws_sdk_mediaconnect.types.vpc_router_network_interface_configuration


class _RouterNetworkInterfaceConfiguration_Public(TypedDict):
    Public: "aws_sdk_mediaconnect.types.public_router_network_interface_configuration.PublicRouterNetworkInterfaceConfiguration"


class _RouterNetworkInterfaceConfiguration_Vpc(TypedDict):
    Vpc: "aws_sdk_mediaconnect.types.vpc_router_network_interface_configuration.VpcRouterNetworkInterfaceConfiguration"


RouterNetworkInterfaceConfiguration: TypeAlias = (
    _RouterNetworkInterfaceConfiguration_Public
    | _RouterNetworkInterfaceConfiguration_Vpc
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceConfiguration) -> dict:
    if "Public" in value:
        import aws_sdk_mediaconnect.types.public_router_network_interface_configuration

        return {
            "public": aws_sdk_mediaconnect.types.public_router_network_interface_configuration.serialize_json(
                value["Public"]
            )
        }
    elif "Vpc" in value:
        import aws_sdk_mediaconnect.types.vpc_router_network_interface_configuration

        return {
            "vpc": aws_sdk_mediaconnect.types.vpc_router_network_interface_configuration.serialize_json(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError(
            "RouterNetworkInterfaceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RouterNetworkInterfaceConfiguration:
    if "public" in data:
        import aws_sdk_mediaconnect.types.public_router_network_interface_configuration

        return {
            "Public": aws_sdk_mediaconnect.types.public_router_network_interface_configuration.deserialize_json(
                data["public"]
            )
        }
    elif "vpc" in data:
        import aws_sdk_mediaconnect.types.vpc_router_network_interface_configuration

        return {
            "Vpc": aws_sdk_mediaconnect.types.vpc_router_network_interface_configuration.deserialize_json(
                data["vpc"]
            )
        }
    else:
        raise DeserializationError(
            "RouterNetworkInterfaceConfiguration: no recognized variant key"
        )
