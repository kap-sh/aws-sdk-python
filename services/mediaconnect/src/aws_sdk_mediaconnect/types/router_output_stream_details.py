"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputStreamDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_connect_flow_router_output_stream_details
    import aws_sdk_mediaconnect.types.media_live_input_router_output_stream_details
    import aws_sdk_mediaconnect.types.standard_router_output_stream_details


class _RouterOutputStreamDetails_Standard(TypedDict, closed=True):
    Standard: "aws_sdk_mediaconnect.types.standard_router_output_stream_details.StandardRouterOutputStreamDetails"


class _RouterOutputStreamDetails_MediaConnectFlow(TypedDict, closed=True):
    MediaConnectFlow: "aws_sdk_mediaconnect.types.media_connect_flow_router_output_stream_details.MediaConnectFlowRouterOutputStreamDetails"


class _RouterOutputStreamDetails_MediaLiveInput(TypedDict, closed=True):
    MediaLiveInput: "aws_sdk_mediaconnect.types.media_live_input_router_output_stream_details.MediaLiveInputRouterOutputStreamDetails"


RouterOutputStreamDetails: TypeAlias = (
    _RouterOutputStreamDetails_Standard
    | _RouterOutputStreamDetails_MediaConnectFlow
    | _RouterOutputStreamDetails_MediaLiveInput
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputStreamDetails) -> dict:
    if "Standard" in value:
        import aws_sdk_mediaconnect.types.standard_router_output_stream_details

        return {
            "standard": aws_sdk_mediaconnect.types.standard_router_output_stream_details.serialize_json(
                value["Standard"]
            )
        }
    elif "MediaConnectFlow" in value:
        import aws_sdk_mediaconnect.types.media_connect_flow_router_output_stream_details

        return {
            "mediaConnectFlow": aws_sdk_mediaconnect.types.media_connect_flow_router_output_stream_details.serialize_json(
                value["MediaConnectFlow"]
            )
        }
    elif "MediaLiveInput" in value:
        import aws_sdk_mediaconnect.types.media_live_input_router_output_stream_details

        return {
            "mediaLiveInput": aws_sdk_mediaconnect.types.media_live_input_router_output_stream_details.serialize_json(
                value["MediaLiveInput"]
            )
        }
    else:
        raise SerializationError("RouterOutputStreamDetails: no variant present")


def deserialize_json(data: dict) -> RouterOutputStreamDetails:
    if "standard" in data:
        import aws_sdk_mediaconnect.types.standard_router_output_stream_details

        return {
            "Standard": aws_sdk_mediaconnect.types.standard_router_output_stream_details.deserialize_json(
                data["standard"]
            )
        }
    elif "mediaConnectFlow" in data:
        import aws_sdk_mediaconnect.types.media_connect_flow_router_output_stream_details

        return {
            "MediaConnectFlow": aws_sdk_mediaconnect.types.media_connect_flow_router_output_stream_details.deserialize_json(
                data["mediaConnectFlow"]
            )
        }
    elif "mediaLiveInput" in data:
        import aws_sdk_mediaconnect.types.media_live_input_router_output_stream_details

        return {
            "MediaLiveInput": aws_sdk_mediaconnect.types.media_live_input_router_output_stream_details.deserialize_json(
                data["mediaLiveInput"]
            )
        }
    else:
        raise DeserializationError(
            "RouterOutputStreamDetails: no recognized variant key"
        )
