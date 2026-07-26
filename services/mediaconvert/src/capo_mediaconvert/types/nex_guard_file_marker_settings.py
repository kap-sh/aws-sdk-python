"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NexGuardFileMarkerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max4194303
    import capo_mediaconvert.types.__string_min1_max256
    import capo_mediaconvert.types.__string_min1_max100000
    import capo_mediaconvert.types.watermarking_strength


class NexGuardFileMarkerSettings(TypedDict, closed=True):
    license: NotRequired[
        "capo_mediaconvert.types.__string_min1_max100000.__stringMin1Max100000"
    ]
    """Use the base64 license string that Nagra provides you. Enter it directly in your JSON job specification or in the console. Required when you include Nagra NexGuard File Marker watermarking in your job."""
    payload: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max4194303.__integerMin0Max4194303"
    ]
    """Specify the payload ID that you want associated with this output. Valid values vary depending on your Nagra NexGuard forensic watermarking workflow. Required when you include Nagra NexGuard File Marker watermarking in your job. For PreRelease Content (NGPR/G2), specify an integer from 1 through 4,194,303. You must generate a unique ID for each asset you watermark, and keep a record of which ID you have assigned to each asset. Neither Nagra nor MediaConvert keep track of the relationship between output files and your IDs. For OTT Streaming, create two adaptive bitrate (ABR) stacks for each asset. Do this by setting up two output groups. For one output group, set the value of Payload ID to 0 in every output. For the other output group, set Payload ID to 1 in every output."""
    preset: NotRequired[
        "capo_mediaconvert.types.__string_min1_max256.__stringMin1Max256"
    ]
    """Enter one of the watermarking preset strings that Nagra provides you. Required when you include Nagra NexGuard File Marker watermarking in your job."""
    strength: NotRequired[
        "capo_mediaconvert.types.watermarking_strength.WatermarkingStrength"
    ]
    """Optional. Ignore this setting unless Nagra support directs you to specify a value. When you don't specify a value here, the Nagra NexGuard library uses its default value."""


# --- restJson1 ser/de ---
def serialize_json(value: NexGuardFileMarkerSettings) -> dict:
    out: dict = {}
    if "license" in value:
        out["license"] = value["license"]
    if "payload" in value:
        out["payload"] = value["payload"]
    if "preset" in value:
        out["preset"] = value["preset"]
    if "strength" in value:
        import capo_mediaconvert.types.watermarking_strength

        out["strength"] = capo_mediaconvert.types.watermarking_strength.serialize_json(
            value["strength"]
        )
    return out


def deserialize_json(data: dict) -> NexGuardFileMarkerSettings:
    out: NexGuardFileMarkerSettings = {}  # type: ignore[typeddict-item]
    if "license" in data:
        out["license"] = data["license"]
    if "payload" in data:
        out["payload"] = data["payload"]
    if "preset" in data:
        out["preset"] = data["preset"]
    if "strength" in data:
        import capo_mediaconvert.types.watermarking_strength

        out["strength"] = (
            capo_mediaconvert.types.watermarking_strength.deserialize_json(
                data["strength"]
            )
        )
    return out
