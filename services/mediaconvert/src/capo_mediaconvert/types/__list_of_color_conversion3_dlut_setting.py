"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfColorConversion3DLUTSetting``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.color_conversion3_dlut_setting

__listOfColorConversion3DLUTSetting: TypeAlias = list[
    "capo_mediaconvert.types.color_conversion3_dlut_setting.ColorConversion3DLUTSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfColorConversion3DLUTSetting) -> list:
    import capo_mediaconvert.types.color_conversion3_dlut_setting

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.color_conversion3_dlut_setting.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfColorConversion3DLUTSetting:
    import capo_mediaconvert.types.color_conversion3_dlut_setting

    out: __listOfColorConversion3DLUTSetting = []
    for item in data:
        out.append(
            capo_mediaconvert.types.color_conversion3_dlut_setting.deserialize_json(
                item
            )
        )
    return out
