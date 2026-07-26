"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfNdiDiscoveryServerConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.ndi_discovery_server_config

__listOfNdiDiscoveryServerConfig: TypeAlias = list[
    "capo_mediaconnect.types.ndi_discovery_server_config.NdiDiscoveryServerConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfNdiDiscoveryServerConfig) -> list:
    import capo_mediaconnect.types.ndi_discovery_server_config

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.ndi_discovery_server_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfNdiDiscoveryServerConfig:
    import capo_mediaconnect.types.ndi_discovery_server_config

    out: __listOfNdiDiscoveryServerConfig = []
    for item in data:
        out.append(
            capo_mediaconnect.types.ndi_discovery_server_config.deserialize_json(item)
        )
    return out
