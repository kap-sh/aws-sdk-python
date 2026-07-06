"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.failover_router_input_configuration
    import aws_sdk_mediaconnect.types.media_connect_flow_router_input_configuration
    import aws_sdk_mediaconnect.types.media_live_channel_router_input_configuration
    import aws_sdk_mediaconnect.types.merge_router_input_configuration
    import aws_sdk_mediaconnect.types.standard_router_input_configuration


class _RouterInputConfiguration_Standard(TypedDict, closed=True):
    Standard: "aws_sdk_mediaconnect.types.standard_router_input_configuration.StandardRouterInputConfiguration"


class _RouterInputConfiguration_MediaLiveChannel(TypedDict, closed=True):
    MediaLiveChannel: "aws_sdk_mediaconnect.types.media_live_channel_router_input_configuration.MediaLiveChannelRouterInputConfiguration"


class _RouterInputConfiguration_Failover(TypedDict, closed=True):
    Failover: "aws_sdk_mediaconnect.types.failover_router_input_configuration.FailoverRouterInputConfiguration"


class _RouterInputConfiguration_MediaConnectFlow(TypedDict, closed=True):
    MediaConnectFlow: "aws_sdk_mediaconnect.types.media_connect_flow_router_input_configuration.MediaConnectFlowRouterInputConfiguration"


class _RouterInputConfiguration_Merge(TypedDict, closed=True):
    Merge: "aws_sdk_mediaconnect.types.merge_router_input_configuration.MergeRouterInputConfiguration"


RouterInputConfiguration: TypeAlias = (
    _RouterInputConfiguration_Standard
    | _RouterInputConfiguration_MediaLiveChannel
    | _RouterInputConfiguration_Failover
    | _RouterInputConfiguration_MediaConnectFlow
    | _RouterInputConfiguration_Merge
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputConfiguration) -> dict:
    if "Standard" in value:
        import aws_sdk_mediaconnect.types.standard_router_input_configuration

        return {
            "standard": aws_sdk_mediaconnect.types.standard_router_input_configuration.serialize_json(
                value["Standard"]
            )
        }
    elif "MediaLiveChannel" in value:
        import aws_sdk_mediaconnect.types.media_live_channel_router_input_configuration

        return {
            "mediaLiveChannel": aws_sdk_mediaconnect.types.media_live_channel_router_input_configuration.serialize_json(
                value["MediaLiveChannel"]
            )
        }
    elif "Failover" in value:
        import aws_sdk_mediaconnect.types.failover_router_input_configuration

        return {
            "failover": aws_sdk_mediaconnect.types.failover_router_input_configuration.serialize_json(
                value["Failover"]
            )
        }
    elif "MediaConnectFlow" in value:
        import aws_sdk_mediaconnect.types.media_connect_flow_router_input_configuration

        return {
            "mediaConnectFlow": aws_sdk_mediaconnect.types.media_connect_flow_router_input_configuration.serialize_json(
                value["MediaConnectFlow"]
            )
        }
    elif "Merge" in value:
        import aws_sdk_mediaconnect.types.merge_router_input_configuration

        return {
            "merge": aws_sdk_mediaconnect.types.merge_router_input_configuration.serialize_json(
                value["Merge"]
            )
        }
    else:
        raise SerializationError("RouterInputConfiguration: no variant present")


def deserialize_json(data: dict) -> RouterInputConfiguration:
    if "standard" in data:
        import aws_sdk_mediaconnect.types.standard_router_input_configuration

        return {
            "Standard": aws_sdk_mediaconnect.types.standard_router_input_configuration.deserialize_json(
                data["standard"]
            )
        }
    elif "mediaLiveChannel" in data:
        import aws_sdk_mediaconnect.types.media_live_channel_router_input_configuration

        return {
            "MediaLiveChannel": aws_sdk_mediaconnect.types.media_live_channel_router_input_configuration.deserialize_json(
                data["mediaLiveChannel"]
            )
        }
    elif "failover" in data:
        import aws_sdk_mediaconnect.types.failover_router_input_configuration

        return {
            "Failover": aws_sdk_mediaconnect.types.failover_router_input_configuration.deserialize_json(
                data["failover"]
            )
        }
    elif "mediaConnectFlow" in data:
        import aws_sdk_mediaconnect.types.media_connect_flow_router_input_configuration

        return {
            "MediaConnectFlow": aws_sdk_mediaconnect.types.media_connect_flow_router_input_configuration.deserialize_json(
                data["mediaConnectFlow"]
            )
        }
    elif "merge" in data:
        import aws_sdk_mediaconnect.types.merge_router_input_configuration

        return {
            "Merge": aws_sdk_mediaconnect.types.merge_router_input_configuration.deserialize_json(
                data["merge"]
            )
        }
    else:
        raise DeserializationError(
            "RouterInputConfiguration: no recognized variant key"
        )
