"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#OriginEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.origin_endpoint_list_configuration

OriginEndpointsList: TypeAlias = list[
    "capo_mediapackagev2.types.origin_endpoint_list_configuration.OriginEndpointListConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: OriginEndpointsList) -> list:
    import capo_mediapackagev2.types.origin_endpoint_list_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.origin_endpoint_list_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OriginEndpointsList:
    import capo_mediapackagev2.types.origin_endpoint_list_configuration

    out: OriginEndpointsList = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.origin_endpoint_list_configuration.deserialize_json(
                item
            )
        )
    return out
