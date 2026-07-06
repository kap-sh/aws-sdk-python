"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Artwork``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.digits_or_auto
    import aws_sdk_elastic_transcoder.types.encryption
    import aws_sdk_elastic_transcoder.types.jpg_or_png
    import aws_sdk_elastic_transcoder.types.padding_policy
    import aws_sdk_elastic_transcoder.types.sizing_policy
    import aws_sdk_elastic_transcoder.types.watermark_key


class Artwork(TypedDict, closed=True):
    input_key: NotRequired[
        "aws_sdk_elastic_transcoder.types.watermark_key.WatermarkKey"
    ]
    """<p>The name of the file to be used as album art. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by <code>PipelineId</code>; the <code>InputBucket</code> object in that pipeline identifies the bucket.</p> <p>If the file name includes a prefix, for example, <code>cooking/pie.jpg</code>, include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.</p>"""
    max_width: NotRequired[
        "aws_sdk_elastic_transcoder.types.digits_or_auto.DigitsOrAuto"
    ]
    """<p>The maximum width of the output album art in pixels. If you specify <code>auto</code>, Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.</p>"""
    max_height: NotRequired[
        "aws_sdk_elastic_transcoder.types.digits_or_auto.DigitsOrAuto"
    ]
    """<p>The maximum height of the output album art in pixels. If you specify <code>auto</code>, Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.</p>"""
    sizing_policy: NotRequired[
        "aws_sdk_elastic_transcoder.types.sizing_policy.SizingPolicy"
    ]
    """<p>Specify one of the following values to control scaling of the output album art:</p> <ul> <li> <p> <code>Fit:</code> Elastic Transcoder scales the output art so it matches the value that you specified in either <code>MaxWidth</code> or <code>MaxHeight</code> without exceeding the other value.</p> </li> <li> <p> <code>Fill:</code> Elastic Transcoder scales the output art so it matches the value that you specified in either <code>MaxWidth</code> or <code>MaxHeight</code> and matches or exceeds the other value. Elastic Transcoder centers the output art and then crops it in the dimension (if any) that exceeds the maximum value. </p> </li> <li> <p> <code>Stretch:</code> Elastic Transcoder stretches the output art to match the values that you specified for <code>MaxWidth</code> and <code>MaxHeight</code>. If the relative proportions of the input art and the output art are different, the output art will be distorted.</p> </li> <li> <p> <code>Keep:</code> Elastic Transcoder does not scale the output art. If either dimension of the input art exceeds the values that you specified for <code>MaxWidth</code> and <code>MaxHeight</code>, Elastic Transcoder crops the output art.</p> </li> <li> <p> <code>ShrinkToFit:</code> Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of <code>MaxWidth</code> and <code>MaxHeight</code> without exceeding either value. If you specify this option, Elastic Transcoder does not scale the art up.</p> </li> <li> <p> <code>ShrinkToFill</code> Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of <code>MaxWidth</code> and <code>MaxHeight</code> without dropping below either value. If you specify this option, Elastic Transcoder does not scale the art up.</p> </li> </ul>"""
    padding_policy: NotRequired[
        "aws_sdk_elastic_transcoder.types.padding_policy.PaddingPolicy"
    ]
    """<p>When you set <code>PaddingPolicy</code> to <code>Pad</code>, Elastic Transcoder may add white bars to the top and bottom and/or left and right sides of the output album art to make the total size of the output art match the values that you specified for <code>MaxWidth</code> and <code>MaxHeight</code>.</p>"""
    album_art_format: NotRequired[
        "aws_sdk_elastic_transcoder.types.jpg_or_png.JpgOrPng"
    ]
    """<p>The format of album art, if any. Valid formats are <code>.jpg</code> and <code>.png</code>.</p>"""
    encryption: NotRequired["aws_sdk_elastic_transcoder.types.encryption.Encryption"]
    """<p>The encryption settings, if any, that you want Elastic Transcoder to apply to your artwork.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Artwork) -> dict:
    out: dict = {}
    if "input_key" in value:
        out["InputKey"] = value["input_key"]
    if "max_width" in value:
        out["MaxWidth"] = value["max_width"]
    if "max_height" in value:
        out["MaxHeight"] = value["max_height"]
    if "sizing_policy" in value:
        out["SizingPolicy"] = value["sizing_policy"]
    if "padding_policy" in value:
        out["PaddingPolicy"] = value["padding_policy"]
    if "album_art_format" in value:
        out["AlbumArtFormat"] = value["album_art_format"]
    if "encryption" in value:
        import aws_sdk_elastic_transcoder.types.encryption

        out["Encryption"] = aws_sdk_elastic_transcoder.types.encryption.serialize_json(
            value["encryption"]
        )
    return out


def deserialize_json(data: dict) -> Artwork:
    out: Artwork = {}  # type: ignore[typeddict-item]
    if "InputKey" in data:
        out["input_key"] = data["InputKey"]
    if "MaxWidth" in data:
        out["max_width"] = data["MaxWidth"]
    if "MaxHeight" in data:
        out["max_height"] = data["MaxHeight"]
    if "SizingPolicy" in data:
        out["sizing_policy"] = data["SizingPolicy"]
    if "PaddingPolicy" in data:
        out["padding_policy"] = data["PaddingPolicy"]
    if "AlbumArtFormat" in data:
        out["album_art_format"] = data["AlbumArtFormat"]
    if "Encryption" in data:
        import aws_sdk_elastic_transcoder.types.encryption

        out["encryption"] = (
            aws_sdk_elastic_transcoder.types.encryption.deserialize_json(
                data["Encryption"]
            )
        )
    return out
