"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#PresetWatermarks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.preset_watermark

PresetWatermarks: TypeAlias = list[
    "capo_elastic_transcoder.types.preset_watermark.PresetWatermark"
]


# --- restJson1 ser/de ---
def serialize_json(value: PresetWatermarks) -> list:
    import capo_elastic_transcoder.types.preset_watermark

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.preset_watermark.serialize_json(item))
    return out


def deserialize_json(data: list) -> PresetWatermarks:
    import capo_elastic_transcoder.types.preset_watermark

    out: PresetWatermarks = []
    for item in data:
        out.append(
            capo_elastic_transcoder.types.preset_watermark.deserialize_json(item)
        )
    return out
