"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfListedGatewayInstance``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_gateway_instance

__listOfListedGatewayInstance: TypeAlias = list[
    "aws_sdk_mediaconnect.types.listed_gateway_instance.ListedGatewayInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfListedGatewayInstance) -> list:
    import aws_sdk_mediaconnect.types.listed_gateway_instance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.listed_gateway_instance.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfListedGatewayInstance:
    import aws_sdk_mediaconnect.types.listed_gateway_instance

    out: __listOfListedGatewayInstance = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.listed_gateway_instance.deserialize_json(item)
        )
    return out
