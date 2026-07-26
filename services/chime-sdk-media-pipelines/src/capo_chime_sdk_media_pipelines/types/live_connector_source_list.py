"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.live_connector_source_configuration

LiveConnectorSourceList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.live_connector_source_configuration.LiveConnectorSourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorSourceList) -> list:
    import capo_chime_sdk_media_pipelines.types.live_connector_source_configuration

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.live_connector_source_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LiveConnectorSourceList:
    import capo_chime_sdk_media_pipelines.types.live_connector_source_configuration

    out: LiveConnectorSourceList = []
    for item in data:
        out.append(
            capo_chime_sdk_media_pipelines.types.live_connector_source_configuration.deserialize_json(
                item
            )
        )
    return out
