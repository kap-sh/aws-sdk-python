"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Thumbnails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.aspect_ratio
    import aws_sdk_elastic_transcoder.types.digits
    import aws_sdk_elastic_transcoder.types.digits_or_auto
    import aws_sdk_elastic_transcoder.types.jpg_or_png
    import aws_sdk_elastic_transcoder.types.padding_policy
    import aws_sdk_elastic_transcoder.types.sizing_policy
    import aws_sdk_elastic_transcoder.types.thumbnail_resolution


class Thumbnails(TypedDict):
    format: NotRequired["aws_sdk_elastic_transcoder.types.jpg_or_png.JpgOrPng"]
    """<p>The format of thumbnails, if any. Valid values are <code>jpg</code> and <code>png</code>. </p> <p>You specify whether you want Elastic Transcoder to create thumbnails when you create a job.</p>"""
    interval: NotRequired["aws_sdk_elastic_transcoder.types.digits.Digits"]
    """<p>The approximate number of seconds between thumbnails. Specify an integer value.</p>"""
    resolution: NotRequired[
        "aws_sdk_elastic_transcoder.types.thumbnail_resolution.ThumbnailResolution"
    ]
    """<important> <p>To better control resolution and aspect ratio of thumbnails, we recommend that you use the values <code>MaxWidth</code>, <code>MaxHeight</code>, <code>SizingPolicy</code>, and <code>PaddingPolicy</code> instead of <code>Resolution</code> and <code>AspectRatio</code>. The two groups of settings are mutually exclusive. Do not use them together.</p> </important> <p>The width and height of thumbnail files in pixels. Specify a value in the format <code> <i>width</i> </code> x <code> <i>height</i> </code> where both values are even integers. The values cannot exceed the width and height that you specified in the <code>Video:Resolution</code> object.</p>"""
    aspect_ratio: NotRequired[
        "aws_sdk_elastic_transcoder.types.aspect_ratio.AspectRatio"
    ]
    """<important> <p>To better control resolution and aspect ratio of thumbnails, we recommend that you use the values <code>MaxWidth</code>, <code>MaxHeight</code>, <code>SizingPolicy</code>, and <code>PaddingPolicy</code> instead of <code>Resolution</code> and <code>AspectRatio</code>. The two groups of settings are mutually exclusive. Do not use them together.</p> </important> <p>The aspect ratio of thumbnails. Valid values include:</p> <p> <code>auto</code>, <code>1:1</code>, <code>4:3</code>, <code>3:2</code>, <code>16:9</code> </p> <p>If you specify <code>auto</code>, Elastic Transcoder tries to preserve the aspect ratio of the video in the output file.</p>"""
    max_width: NotRequired[
        "aws_sdk_elastic_transcoder.types.digits_or_auto.DigitsOrAuto"
    ]
    """<p>The maximum width of thumbnails in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 4096.</p>"""
    max_height: NotRequired[
        "aws_sdk_elastic_transcoder.types.digits_or_auto.DigitsOrAuto"
    ]
    """<p>The maximum height of thumbnails in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 3072.</p>"""
    sizing_policy: NotRequired[
        "aws_sdk_elastic_transcoder.types.sizing_policy.SizingPolicy"
    ]
    """<p>Specify one of the following values to control scaling of thumbnails:</p> <ul> <li> <p> <code>Fit</code>: Elastic Transcoder scales thumbnails so they match the value that you specified in thumbnail MaxWidth or MaxHeight settings without exceeding the other value. </p> </li> <li> <p> <code>Fill</code>: Elastic Transcoder scales thumbnails so they match the value that you specified in thumbnail <code>MaxWidth</code> or <code>MaxHeight</code> settings and matches or exceeds the other value. Elastic Transcoder centers the image in thumbnails and then crops in the dimension (if any) that exceeds the maximum value.</p> </li> <li> <p> <code>Stretch</code>: Elastic Transcoder stretches thumbnails to match the values that you specified for thumbnail <code>MaxWidth</code> and <code>MaxHeight</code> settings. If the relative proportions of the input video and thumbnails are different, the thumbnails will be distorted.</p> </li> <li> <p> <code>Keep</code>: Elastic Transcoder does not scale thumbnails. If either dimension of the input video exceeds the values that you specified for thumbnail <code>MaxWidth</code> and <code>MaxHeight</code> settings, Elastic Transcoder crops the thumbnails.</p> </li> <li> <p> <code>ShrinkToFit</code>: Elastic Transcoder scales thumbnails down so that their dimensions match the values that you specified for at least one of thumbnail <code>MaxWidth</code> and <code>MaxHeight</code> without exceeding either value. If you specify this option, Elastic Transcoder does not scale thumbnails up.</p> </li> <li> <p> <code>ShrinkToFill</code>: Elastic Transcoder scales thumbnails down so that their dimensions match the values that you specified for at least one of <code>MaxWidth</code> and <code>MaxHeight</code> without dropping below either value. If you specify this option, Elastic Transcoder does not scale thumbnails up.</p> </li> </ul>"""
    padding_policy: NotRequired[
        "aws_sdk_elastic_transcoder.types.padding_policy.PaddingPolicy"
    ]
    """<p>When you set <code>PaddingPolicy</code> to <code>Pad</code>, Elastic Transcoder may add black bars to the top and bottom and/or left and right sides of thumbnails to make the total size of the thumbnails match the values that you specified for thumbnail <code>MaxWidth</code> and <code>MaxHeight</code> settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Thumbnails) -> dict:
    out: dict = {}
    if "format" in value:
        out["Format"] = value["format"]
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "resolution" in value:
        out["Resolution"] = value["resolution"]
    if "aspect_ratio" in value:
        out["AspectRatio"] = value["aspect_ratio"]
    if "max_width" in value:
        out["MaxWidth"] = value["max_width"]
    if "max_height" in value:
        out["MaxHeight"] = value["max_height"]
    if "sizing_policy" in value:
        out["SizingPolicy"] = value["sizing_policy"]
    if "padding_policy" in value:
        out["PaddingPolicy"] = value["padding_policy"]
    return out


def deserialize_json(data: dict) -> Thumbnails:
    out: Thumbnails = {}  # type: ignore[typeddict-item]
    if "Format" in data:
        out["format"] = data["Format"]
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "Resolution" in data:
        out["resolution"] = data["Resolution"]
    if "AspectRatio" in data:
        out["aspect_ratio"] = data["AspectRatio"]
    if "MaxWidth" in data:
        out["max_width"] = data["MaxWidth"]
    if "MaxHeight" in data:
        out["max_height"] = data["MaxHeight"]
    if "SizingPolicy" in data:
        out["sizing_policy"] = data["SizingPolicy"]
    if "PaddingPolicy" in data:
        out["padding_policy"] = data["PaddingPolicy"]
    return out
