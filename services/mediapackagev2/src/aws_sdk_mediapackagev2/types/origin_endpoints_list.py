"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#OriginEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.origin_endpoint_list_configuration

OriginEndpointsList: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.origin_endpoint_list_configuration.OriginEndpointListConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: OriginEndpointsList) -> list:
    import aws_sdk_mediapackagev2.types.origin_endpoint_list_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.origin_endpoint_list_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OriginEndpointsList:
    import aws_sdk_mediapackagev2.types.origin_endpoint_list_configuration

    out: OriginEndpointsList = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.origin_endpoint_list_configuration.deserialize_json(
                item
            )
        )
    return out
