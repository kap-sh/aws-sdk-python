"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputStreamDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.failover_router_input_stream_details
    import aws_sdk_mediaconnect.types.media_connect_flow_router_input_stream_details
    import aws_sdk_mediaconnect.types.media_live_channel_router_input_stream_details
    import aws_sdk_mediaconnect.types.merge_router_input_stream_details
    import aws_sdk_mediaconnect.types.standard_router_input_stream_details


class _RouterInputStreamDetails_Standard(TypedDict):
    Standard: "aws_sdk_mediaconnect.types.standard_router_input_stream_details.StandardRouterInputStreamDetails"


class _RouterInputStreamDetails_MediaLiveChannel(TypedDict):
    MediaLiveChannel: "aws_sdk_mediaconnect.types.media_live_channel_router_input_stream_details.MediaLiveChannelRouterInputStreamDetails"


class _RouterInputStreamDetails_Failover(TypedDict):
    Failover: "aws_sdk_mediaconnect.types.failover_router_input_stream_details.FailoverRouterInputStreamDetails"


class _RouterInputStreamDetails_MediaConnectFlow(TypedDict):
    MediaConnectFlow: "aws_sdk_mediaconnect.types.media_connect_flow_router_input_stream_details.MediaConnectFlowRouterInputStreamDetails"


class _RouterInputStreamDetails_Merge(TypedDict):
    Merge: "aws_sdk_mediaconnect.types.merge_router_input_stream_details.MergeRouterInputStreamDetails"


RouterInputStreamDetails: TypeAlias = (
    _RouterInputStreamDetails_Standard
    | _RouterInputStreamDetails_MediaLiveChannel
    | _RouterInputStreamDetails_Failover
    | _RouterInputStreamDetails_MediaConnectFlow
    | _RouterInputStreamDetails_Merge
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputStreamDetails) -> dict:
    if "Standard" in value:
        import aws_sdk_mediaconnect.types.standard_router_input_stream_details

        return {
            "standard": aws_sdk_mediaconnect.types.standard_router_input_stream_details.serialize_json(
                value["Standard"]
            )
        }
    elif "MediaLiveChannel" in value:
        import aws_sdk_mediaconnect.types.media_live_channel_router_input_stream_details

        return {
            "mediaLiveChannel": aws_sdk_mediaconnect.types.media_live_channel_router_input_stream_details.serialize_json(
                value["MediaLiveChannel"]
            )
        }
    elif "Failover" in value:
        import aws_sdk_mediaconnect.types.failover_router_input_stream_details

        return {
            "failover": aws_sdk_mediaconnect.types.failover_router_input_stream_details.serialize_json(
                value["Failover"]
            )
        }
    elif "MediaConnectFlow" in value:
        import aws_sdk_mediaconnect.types.media_connect_flow_router_input_stream_details

        return {
            "mediaConnectFlow": aws_sdk_mediaconnect.types.media_connect_flow_router_input_stream_details.serialize_json(
                value["MediaConnectFlow"]
            )
        }
    elif "Merge" in value:
        import aws_sdk_mediaconnect.types.merge_router_input_stream_details

        return {
            "merge": aws_sdk_mediaconnect.types.merge_router_input_stream_details.serialize_json(
                value["Merge"]
            )
        }
    else:
        raise SerializationError("RouterInputStreamDetails: no variant present")


def deserialize_json(data: dict) -> RouterInputStreamDetails:
    if "standard" in data:
        import aws_sdk_mediaconnect.types.standard_router_input_stream_details

        return {
            "Standard": aws_sdk_mediaconnect.types.standard_router_input_stream_details.deserialize_json(
                data["standard"]
            )
        }
    elif "mediaLiveChannel" in data:
        import aws_sdk_mediaconnect.types.media_live_channel_router_input_stream_details

        return {
            "MediaLiveChannel": aws_sdk_mediaconnect.types.media_live_channel_router_input_stream_details.deserialize_json(
                data["mediaLiveChannel"]
            )
        }
    elif "failover" in data:
        import aws_sdk_mediaconnect.types.failover_router_input_stream_details

        return {
            "Failover": aws_sdk_mediaconnect.types.failover_router_input_stream_details.deserialize_json(
                data["failover"]
            )
        }
    elif "mediaConnectFlow" in data:
        import aws_sdk_mediaconnect.types.media_connect_flow_router_input_stream_details

        return {
            "MediaConnectFlow": aws_sdk_mediaconnect.types.media_connect_flow_router_input_stream_details.deserialize_json(
                data["mediaConnectFlow"]
            )
        }
    elif "merge" in data:
        import aws_sdk_mediaconnect.types.merge_router_input_stream_details

        return {
            "Merge": aws_sdk_mediaconnect.types.merge_router_input_stream_details.deserialize_json(
                data["merge"]
            )
        }
    else:
        raise DeserializationError(
            "RouterInputStreamDetails: no recognized variant key"
        )
