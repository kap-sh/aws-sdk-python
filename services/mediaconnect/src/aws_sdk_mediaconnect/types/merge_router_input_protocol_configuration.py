"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MergeRouterInputProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.rist_router_input_configuration
    import aws_sdk_mediaconnect.types.rtp_router_input_configuration


class _MergeRouterInputProtocolConfiguration_Rtp(TypedDict, closed=True):
    Rtp: "aws_sdk_mediaconnect.types.rtp_router_input_configuration.RtpRouterInputConfiguration"


class _MergeRouterInputProtocolConfiguration_Rist(TypedDict, closed=True):
    Rist: "aws_sdk_mediaconnect.types.rist_router_input_configuration.RistRouterInputConfiguration"


MergeRouterInputProtocolConfiguration: TypeAlias = (
    _MergeRouterInputProtocolConfiguration_Rtp
    | _MergeRouterInputProtocolConfiguration_Rist
)


# --- restJson1 ser/de ---
def serialize_json(value: MergeRouterInputProtocolConfiguration) -> dict:
    if "Rtp" in value:
        import aws_sdk_mediaconnect.types.rtp_router_input_configuration

        return {
            "rtp": aws_sdk_mediaconnect.types.rtp_router_input_configuration.serialize_json(
                value["Rtp"]
            )
        }
    elif "Rist" in value:
        import aws_sdk_mediaconnect.types.rist_router_input_configuration

        return {
            "rist": aws_sdk_mediaconnect.types.rist_router_input_configuration.serialize_json(
                value["Rist"]
            )
        }
    else:
        raise SerializationError(
            "MergeRouterInputProtocolConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MergeRouterInputProtocolConfiguration:
    if "rtp" in data:
        import aws_sdk_mediaconnect.types.rtp_router_input_configuration

        return {
            "Rtp": aws_sdk_mediaconnect.types.rtp_router_input_configuration.deserialize_json(
                data["rtp"]
            )
        }
    elif "rist" in data:
        import aws_sdk_mediaconnect.types.rist_router_input_configuration

        return {
            "Rist": aws_sdk_mediaconnect.types.rist_router_input_configuration.deserialize_json(
                data["rist"]
            )
        }
    else:
        raise DeserializationError(
            "MergeRouterInputProtocolConfiguration: no recognized variant key"
        )
