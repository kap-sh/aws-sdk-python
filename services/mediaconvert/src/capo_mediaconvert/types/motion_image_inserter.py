"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MotionImageInserter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_min11_max11_pattern01_d20305_d205_d
    import capo_mediaconvert.types.__string_min14_pattern_s3_mov09_png_https_mov09_png
    import capo_mediaconvert.types.motion_image_insertion_framerate
    import capo_mediaconvert.types.motion_image_insertion_mode
    import capo_mediaconvert.types.motion_image_insertion_offset
    import capo_mediaconvert.types.motion_image_playback


class MotionImageInserter(TypedDict, closed=True):
    framerate: NotRequired[
        "capo_mediaconvert.types.motion_image_insertion_framerate.MotionImageInsertionFramerate"
    ]
    """If your motion graphic asset is a .mov file, keep this setting unspecified. If your motion graphic asset is a series of .png files, specify the frame rate of the overlay in frames per second, as a fraction. For example, specify 24 fps as 24/1. Make sure that the number of images in your series matches the frame rate and your intended overlay duration. For example, if you want a 30-second overlay at 30 fps, you should have 900 .png images. This overlay frame rate doesn't need to match the frame rate of the underlying video."""
    input: NotRequired[
        "capo_mediaconvert.types.__string_min14_pattern_s3_mov09_png_https_mov09_png.__stringMin14PatternS3Mov09PngHttpsMov09Png"
    ]
    """Specify the .mov file or series of .png files that you want to overlay on your video. For .png files, provide the file name of the first file in the series. Make sure that the names of the .png files end with sequential numbers that specify the order that they are played in. For example, overlay_000.png, overlay_001.png, overlay_002.png, and so on. The sequence must start at zero, and each image file name must have the same number of digits. Pad your initial file names with enough zeros to complete the sequence. For example, if the first image is overlay_0.png, there can be only 10 images in the sequence, with the last image being overlay_9.png. But if the first image is overlay_00.png, there can be 100 images in the sequence."""
    insertion_mode: NotRequired[
        "capo_mediaconvert.types.motion_image_insertion_mode.MotionImageInsertionMode"
    ]
    """Choose the type of motion graphic asset that you are providing for your overlay. You can choose either a .mov file or a series of .png files."""
    offset: NotRequired[
        "capo_mediaconvert.types.motion_image_insertion_offset.MotionImageInsertionOffset"
    ]
    """Use Offset to specify the placement of your motion graphic overlay on the video frame. Specify in pixels, from the upper-left corner of the frame. If you don't specify an offset, the service scales your overlay to the full size of the frame. Otherwise, the service inserts the overlay at its native resolution and scales the size up or down with any video scaling."""
    playback: NotRequired[
        "capo_mediaconvert.types.motion_image_playback.MotionImagePlayback"
    ]
    """Specify whether your motion graphic overlay repeats on a loop or plays only once."""
    start_time: NotRequired[
        "capo_mediaconvert.types.__string_min11_max11_pattern01_d20305_d205_d.__stringMin11Max11Pattern01D20305D205D"
    ]
    """Specify when the motion overlay begins. Use timecode format (HH:MM:SS:FF or HH:MM:SS;FF). Make sure that the timecode you provide here takes into account how you have set up your timecode configuration under both job settings and input settings. The simplest way to do that is to set both to start at 0. If you need to set up your job to follow timecodes embedded in your source that don't start at zero, make sure that you specify a start time that is after the first embedded timecode. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-timecode.html"""


# --- restJson1 ser/de ---
def serialize_json(value: MotionImageInserter) -> dict:
    out: dict = {}
    if "framerate" in value:
        import capo_mediaconvert.types.motion_image_insertion_framerate

        out["framerate"] = (
            capo_mediaconvert.types.motion_image_insertion_framerate.serialize_json(
                value["framerate"]
            )
        )
    if "input" in value:
        out["input"] = value["input"]
    if "insertion_mode" in value:
        import capo_mediaconvert.types.motion_image_insertion_mode

        out["insertionMode"] = (
            capo_mediaconvert.types.motion_image_insertion_mode.serialize_json(
                value["insertion_mode"]
            )
        )
    if "offset" in value:
        import capo_mediaconvert.types.motion_image_insertion_offset

        out["offset"] = (
            capo_mediaconvert.types.motion_image_insertion_offset.serialize_json(
                value["offset"]
            )
        )
    if "playback" in value:
        import capo_mediaconvert.types.motion_image_playback

        out["playback"] = capo_mediaconvert.types.motion_image_playback.serialize_json(
            value["playback"]
        )
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    return out


def deserialize_json(data: dict) -> MotionImageInserter:
    out: MotionImageInserter = {}  # type: ignore[typeddict-item]
    if "framerate" in data:
        import capo_mediaconvert.types.motion_image_insertion_framerate

        out["framerate"] = (
            capo_mediaconvert.types.motion_image_insertion_framerate.deserialize_json(
                data["framerate"]
            )
        )
    if "input" in data:
        out["input"] = data["input"]
    if "insertionMode" in data:
        import capo_mediaconvert.types.motion_image_insertion_mode

        out["insertion_mode"] = (
            capo_mediaconvert.types.motion_image_insertion_mode.deserialize_json(
                data["insertionMode"]
            )
        )
    if "offset" in data:
        import capo_mediaconvert.types.motion_image_insertion_offset

        out["offset"] = (
            capo_mediaconvert.types.motion_image_insertion_offset.deserialize_json(
                data["offset"]
            )
        )
    if "playback" in data:
        import capo_mediaconvert.types.motion_image_playback

        out["playback"] = (
            capo_mediaconvert.types.motion_image_playback.deserialize_json(
                data["playback"]
            )
        )
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    return out
