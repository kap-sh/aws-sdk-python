"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CompositionThumbnailConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.composition_thumbnail_configuration

CompositionThumbnailConfigurationList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.composition_thumbnail_configuration.CompositionThumbnailConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositionThumbnailConfigurationList) -> list:
    import aws_sdk_ivs_realtime.types.composition_thumbnail_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.composition_thumbnail_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CompositionThumbnailConfigurationList:
    import aws_sdk_ivs_realtime.types.composition_thumbnail_configuration

    out: CompositionThumbnailConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.composition_thumbnail_configuration.deserialize_json(
                item
            )
        )
    return out
