"""Generated from Smithy shape ``com.amazonaws.ivs#RenditionConfigurationRenditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.rendition_configuration_rendition

RenditionConfigurationRenditionList: TypeAlias = list[
    "capo_ivs.types.rendition_configuration_rendition.RenditionConfigurationRendition"
]


# --- restJson1 ser/de ---
def serialize_json(value: RenditionConfigurationRenditionList) -> list:
    import capo_ivs.types.rendition_configuration_rendition

    out: list = []
    for item in value:
        out.append(
            capo_ivs.types.rendition_configuration_rendition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RenditionConfigurationRenditionList:
    import capo_ivs.types.rendition_configuration_rendition

    out: RenditionConfigurationRenditionList = []
    for item in data:
        out.append(
            capo_ivs.types.rendition_configuration_rendition.deserialize_json(item)
        )
    return out
