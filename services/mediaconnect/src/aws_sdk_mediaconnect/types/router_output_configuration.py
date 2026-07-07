"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_connect_flow_router_output_configuration
    import aws_sdk_mediaconnect.types.media_live_input_router_output_configuration
    import aws_sdk_mediaconnect.types.standard_router_output_configuration


class _RouterOutputConfiguration_Standard(TypedDict, closed=True):
    Standard: "aws_sdk_mediaconnect.types.standard_router_output_configuration.StandardRouterOutputConfiguration"


class _RouterOutputConfiguration_MediaConnectFlow(TypedDict, closed=True):
    MediaConnectFlow: "aws_sdk_mediaconnect.types.media_connect_flow_router_output_configuration.MediaConnectFlowRouterOutputConfiguration"


class _RouterOutputConfiguration_MediaLiveInput(TypedDict, closed=True):
    MediaLiveInput: "aws_sdk_mediaconnect.types.media_live_input_router_output_configuration.MediaLiveInputRouterOutputConfiguration"


RouterOutputConfiguration: TypeAlias = (
    _RouterOutputConfiguration_Standard
    | _RouterOutputConfiguration_MediaConnectFlow
    | _RouterOutputConfiguration_MediaLiveInput
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputConfiguration) -> dict:
    if "Standard" in value:
        import aws_sdk_mediaconnect.types.standard_router_output_configuration

        return {
            "standard": aws_sdk_mediaconnect.types.standard_router_output_configuration.serialize_json(
                value["Standard"]
            )
        }
    elif "MediaConnectFlow" in value:
        import aws_sdk_mediaconnect.types.media_connect_flow_router_output_configuration

        return {
            "mediaConnectFlow": aws_sdk_mediaconnect.types.media_connect_flow_router_output_configuration.serialize_json(
                value["MediaConnectFlow"]
            )
        }
    elif "MediaLiveInput" in value:
        import aws_sdk_mediaconnect.types.media_live_input_router_output_configuration

        return {
            "mediaLiveInput": aws_sdk_mediaconnect.types.media_live_input_router_output_configuration.serialize_json(
                value["MediaLiveInput"]
            )
        }
    else:
        raise SerializationError("RouterOutputConfiguration: no variant present")


def deserialize_json(data: dict) -> RouterOutputConfiguration:
    if "standard" in data:
        import aws_sdk_mediaconnect.types.standard_router_output_configuration

        return {
            "Standard": aws_sdk_mediaconnect.types.standard_router_output_configuration.deserialize_json(
                data["standard"]
            )
        }
    elif "mediaConnectFlow" in data:
        import aws_sdk_mediaconnect.types.media_connect_flow_router_output_configuration

        return {
            "MediaConnectFlow": aws_sdk_mediaconnect.types.media_connect_flow_router_output_configuration.deserialize_json(
                data["mediaConnectFlow"]
            )
        }
    elif "mediaLiveInput" in data:
        import aws_sdk_mediaconnect.types.media_live_input_router_output_configuration

        return {
            "MediaLiveInput": aws_sdk_mediaconnect.types.media_live_input_router_output_configuration.deserialize_json(
                data["mediaLiveInput"]
            )
        }
    else:
        raise DeserializationError(
            "RouterOutputConfiguration: no recognized variant key"
        )
