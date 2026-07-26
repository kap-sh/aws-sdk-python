"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcSpatialAdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

"""The best way to set up adaptive quantization is to keep the default value, Auto, for the setting Adaptive quantization. When you do so, MediaConvert automatically applies the best types of quantization for your video content. Include this setting in your JSON job specification only when you choose to change the default value for Adaptive quantization. For this setting, keep the default value, Enabled, to adjust quantization within each frame based on spatial variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas that can sustain more distortion with no noticeable visual degradation and uses more bits on areas where any small distortion will be noticeable. For example, complex textured blocks are encoded with fewer bits and smooth textured blocks are encoded with more bits. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen with a lot of complex texture, you might choose to disable this feature. Related setting: When you enable spatial adaptive quantization, set the value for Adaptive quantization depending on your content. For homogeneous content, such as cartoons and video games, set it to Low. For content with a wider variety of textures, set it to High or Higher."""
XavcSpatialAdaptiveQuantization: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: XavcSpatialAdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> XavcSpatialAdaptiveQuantization:
    return cast(XavcSpatialAdaptiveQuantization, data)
