"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.rist_router_input_configuration
    import aws_sdk_mediaconnect.types.rtp_router_input_configuration
    import aws_sdk_mediaconnect.types.srt_caller_router_input_configuration
    import aws_sdk_mediaconnect.types.srt_listener_router_input_configuration


class _FailoverRouterInputProtocolConfiguration_Rist(TypedDict, closed=True):
    Rist: "aws_sdk_mediaconnect.types.rist_router_input_configuration.RistRouterInputConfiguration"


class _FailoverRouterInputProtocolConfiguration_SrtListener(TypedDict, closed=True):
    SrtListener: "aws_sdk_mediaconnect.types.srt_listener_router_input_configuration.SrtListenerRouterInputConfiguration"


class _FailoverRouterInputProtocolConfiguration_SrtCaller(TypedDict, closed=True):
    SrtCaller: "aws_sdk_mediaconnect.types.srt_caller_router_input_configuration.SrtCallerRouterInputConfiguration"


class _FailoverRouterInputProtocolConfiguration_Rtp(TypedDict, closed=True):
    Rtp: "aws_sdk_mediaconnect.types.rtp_router_input_configuration.RtpRouterInputConfiguration"


FailoverRouterInputProtocolConfiguration: TypeAlias = (
    _FailoverRouterInputProtocolConfiguration_Rist
    | _FailoverRouterInputProtocolConfiguration_SrtListener
    | _FailoverRouterInputProtocolConfiguration_SrtCaller
    | _FailoverRouterInputProtocolConfiguration_Rtp
)


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputProtocolConfiguration) -> dict:
    if "Rist" in value:
        import aws_sdk_mediaconnect.types.rist_router_input_configuration

        return {
            "rist": aws_sdk_mediaconnect.types.rist_router_input_configuration.serialize_json(
                value["Rist"]
            )
        }
    elif "SrtListener" in value:
        import aws_sdk_mediaconnect.types.srt_listener_router_input_configuration

        return {
            "srtListener": aws_sdk_mediaconnect.types.srt_listener_router_input_configuration.serialize_json(
                value["SrtListener"]
            )
        }
    elif "SrtCaller" in value:
        import aws_sdk_mediaconnect.types.srt_caller_router_input_configuration

        return {
            "srtCaller": aws_sdk_mediaconnect.types.srt_caller_router_input_configuration.serialize_json(
                value["SrtCaller"]
            )
        }
    elif "Rtp" in value:
        import aws_sdk_mediaconnect.types.rtp_router_input_configuration

        return {
            "rtp": aws_sdk_mediaconnect.types.rtp_router_input_configuration.serialize_json(
                value["Rtp"]
            )
        }
    else:
        raise SerializationError(
            "FailoverRouterInputProtocolConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> FailoverRouterInputProtocolConfiguration:
    if "rist" in data:
        import aws_sdk_mediaconnect.types.rist_router_input_configuration

        return {
            "Rist": aws_sdk_mediaconnect.types.rist_router_input_configuration.deserialize_json(
                data["rist"]
            )
        }
    elif "srtListener" in data:
        import aws_sdk_mediaconnect.types.srt_listener_router_input_configuration

        return {
            "SrtListener": aws_sdk_mediaconnect.types.srt_listener_router_input_configuration.deserialize_json(
                data["srtListener"]
            )
        }
    elif "srtCaller" in data:
        import aws_sdk_mediaconnect.types.srt_caller_router_input_configuration

        return {
            "SrtCaller": aws_sdk_mediaconnect.types.srt_caller_router_input_configuration.deserialize_json(
                data["srtCaller"]
            )
        }
    elif "rtp" in data:
        import aws_sdk_mediaconnect.types.rtp_router_input_configuration

        return {
            "Rtp": aws_sdk_mediaconnect.types.rtp_router_input_configuration.deserialize_json(
                data["rtp"]
            )
        }
    else:
        raise DeserializationError(
            "FailoverRouterInputProtocolConfiguration: no recognized variant key"
        )
