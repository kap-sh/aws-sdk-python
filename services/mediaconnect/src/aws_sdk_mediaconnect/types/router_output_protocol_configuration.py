"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.rist_router_output_configuration
    import aws_sdk_mediaconnect.types.rtp_router_output_configuration
    import aws_sdk_mediaconnect.types.srt_caller_router_output_configuration
    import aws_sdk_mediaconnect.types.srt_listener_router_output_configuration


class _RouterOutputProtocolConfiguration_Rist(TypedDict):
    Rist: "aws_sdk_mediaconnect.types.rist_router_output_configuration.RistRouterOutputConfiguration"


class _RouterOutputProtocolConfiguration_SrtListener(TypedDict):
    SrtListener: "aws_sdk_mediaconnect.types.srt_listener_router_output_configuration.SrtListenerRouterOutputConfiguration"


class _RouterOutputProtocolConfiguration_SrtCaller(TypedDict):
    SrtCaller: "aws_sdk_mediaconnect.types.srt_caller_router_output_configuration.SrtCallerRouterOutputConfiguration"


class _RouterOutputProtocolConfiguration_Rtp(TypedDict):
    Rtp: "aws_sdk_mediaconnect.types.rtp_router_output_configuration.RtpRouterOutputConfiguration"


RouterOutputProtocolConfiguration: TypeAlias = (
    _RouterOutputProtocolConfiguration_Rist
    | _RouterOutputProtocolConfiguration_SrtListener
    | _RouterOutputProtocolConfiguration_SrtCaller
    | _RouterOutputProtocolConfiguration_Rtp
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputProtocolConfiguration) -> dict:
    if "Rist" in value:
        import aws_sdk_mediaconnect.types.rist_router_output_configuration

        return {
            "rist": aws_sdk_mediaconnect.types.rist_router_output_configuration.serialize_json(
                value["Rist"]
            )
        }
    elif "SrtListener" in value:
        import aws_sdk_mediaconnect.types.srt_listener_router_output_configuration

        return {
            "srtListener": aws_sdk_mediaconnect.types.srt_listener_router_output_configuration.serialize_json(
                value["SrtListener"]
            )
        }
    elif "SrtCaller" in value:
        import aws_sdk_mediaconnect.types.srt_caller_router_output_configuration

        return {
            "srtCaller": aws_sdk_mediaconnect.types.srt_caller_router_output_configuration.serialize_json(
                value["SrtCaller"]
            )
        }
    elif "Rtp" in value:
        import aws_sdk_mediaconnect.types.rtp_router_output_configuration

        return {
            "rtp": aws_sdk_mediaconnect.types.rtp_router_output_configuration.serialize_json(
                value["Rtp"]
            )
        }
    else:
        raise SerializationError(
            "RouterOutputProtocolConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RouterOutputProtocolConfiguration:
    if "rist" in data:
        import aws_sdk_mediaconnect.types.rist_router_output_configuration

        return {
            "Rist": aws_sdk_mediaconnect.types.rist_router_output_configuration.deserialize_json(
                data["rist"]
            )
        }
    elif "srtListener" in data:
        import aws_sdk_mediaconnect.types.srt_listener_router_output_configuration

        return {
            "SrtListener": aws_sdk_mediaconnect.types.srt_listener_router_output_configuration.deserialize_json(
                data["srtListener"]
            )
        }
    elif "srtCaller" in data:
        import aws_sdk_mediaconnect.types.srt_caller_router_output_configuration

        return {
            "SrtCaller": aws_sdk_mediaconnect.types.srt_caller_router_output_configuration.deserialize_json(
                data["srtCaller"]
            )
        }
    elif "rtp" in data:
        import aws_sdk_mediaconnect.types.rtp_router_output_configuration

        return {
            "Rtp": aws_sdk_mediaconnect.types.rtp_router_output_configuration.deserialize_json(
                data["rtp"]
            )
        }
    else:
        raise DeserializationError(
            "RouterOutputProtocolConfiguration: no recognized variant key"
        )
