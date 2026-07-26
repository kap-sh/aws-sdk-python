"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#JobWatermark``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.encryption
    import capo_elastic_transcoder.types.preset_watermark_id
    import capo_elastic_transcoder.types.watermark_key


class JobWatermark(TypedDict, closed=True):
    preset_watermark_id: NotRequired[
        "capo_elastic_transcoder.types.preset_watermark_id.PresetWatermarkId"
    ]
    """<p>The ID of the watermark settings that Elastic Transcoder uses to add watermarks to the video during transcoding. The settings are in the preset specified by Preset for the current output. In that preset, the value of Watermarks Id tells Elastic Transcoder which settings to use.</p>"""
    input_key: NotRequired["capo_elastic_transcoder.types.watermark_key.WatermarkKey"]
    """<p> The name of the .png or .jpg file that you want to use for the watermark. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by <code>Pipeline</code>; the <code>Input Bucket</code> object in that pipeline identifies the bucket.</p> <p> If the file name includes a prefix, for example, <b>logos/128x64.png</b>, include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error. </p>"""
    encryption: NotRequired["capo_elastic_transcoder.types.encryption.Encryption"]
    """<p>The encryption settings, if any, that you want Elastic Transcoder to apply to your watermarks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobWatermark) -> dict:
    out: dict = {}
    if "preset_watermark_id" in value:
        out["PresetWatermarkId"] = value["preset_watermark_id"]
    if "input_key" in value:
        out["InputKey"] = value["input_key"]
    if "encryption" in value:
        import capo_elastic_transcoder.types.encryption

        out["Encryption"] = capo_elastic_transcoder.types.encryption.serialize_json(
            value["encryption"]
        )
    return out


def deserialize_json(data: dict) -> JobWatermark:
    out: JobWatermark = {}  # type: ignore[typeddict-item]
    if "PresetWatermarkId" in data:
        out["preset_watermark_id"] = data["PresetWatermarkId"]
    if "InputKey" in data:
        out["input_key"] = data["InputKey"]
    if "Encryption" in data:
        import capo_elastic_transcoder.types.encryption

        out["encryption"] = capo_elastic_transcoder.types.encryption.deserialize_json(
            data["Encryption"]
        )
    return out
