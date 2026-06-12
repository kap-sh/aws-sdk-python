"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#PresetWatermarks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.preset_watermark

PresetWatermarks: TypeAlias = list[
    "aws_sdk_elastic_transcoder.types.preset_watermark.PresetWatermark"
]


# --- restJson1 ser/de ---
def serialize_json(value: PresetWatermarks) -> list:
    import aws_sdk_elastic_transcoder.types.preset_watermark

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elastic_transcoder.types.preset_watermark.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PresetWatermarks:
    import aws_sdk_elastic_transcoder.types.preset_watermark

    out: PresetWatermarks = []
    for item in data:
        out.append(
            aws_sdk_elastic_transcoder.types.preset_watermark.deserialize_json(item)
        )
    return out
