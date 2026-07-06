"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#JobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.aspect_ratio
    import aws_sdk_elastic_transcoder.types.detected_properties
    import aws_sdk_elastic_transcoder.types.encryption
    import aws_sdk_elastic_transcoder.types.frame_rate
    import aws_sdk_elastic_transcoder.types.input_captions
    import aws_sdk_elastic_transcoder.types.interlaced
    import aws_sdk_elastic_transcoder.types.job_container
    import aws_sdk_elastic_transcoder.types.long_key
    import aws_sdk_elastic_transcoder.types.resolution
    import aws_sdk_elastic_transcoder.types.time_span


class JobInput(TypedDict, closed=True):
    key: NotRequired["aws_sdk_elastic_transcoder.types.long_key.LongKey"]
    """<p> The name of the file to transcode. Elsewhere in the body of the JSON block is the the ID of the pipeline to use for processing the job. The <code>InputBucket</code> object in that pipeline tells Elastic Transcoder which Amazon S3 bucket to get the file from. </p> <p>If the file name includes a prefix, such as <code>cooking/lasagna.mpg</code>, include the prefix in the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.</p>"""
    frame_rate: NotRequired["aws_sdk_elastic_transcoder.types.frame_rate.FrameRate"]
    """<p>The frame rate of the input file. If you want Elastic Transcoder to automatically detect the frame rate of the input file, specify <code>auto</code>. If you want to specify the frame rate for the input file, enter one of the following values: </p> <p> <code>10</code>, <code>15</code>, <code>23.97</code>, <code>24</code>, <code>25</code>, <code>29.97</code>, <code>30</code>, <code>60</code> </p> <p>If you specify a value other than <code>auto</code>, Elastic Transcoder disables automatic detection of the frame rate.</p>"""
    resolution: NotRequired["aws_sdk_elastic_transcoder.types.resolution.Resolution"]
    """<p>This value must be <code>auto</code>, which causes Elastic Transcoder to automatically detect the resolution of the input file.</p>"""
    aspect_ratio: NotRequired[
        "aws_sdk_elastic_transcoder.types.aspect_ratio.AspectRatio"
    ]
    """<p> The aspect ratio of the input file. If you want Elastic Transcoder to automatically detect the aspect ratio of the input file, specify <code>auto</code>. If you want to specify the aspect ratio for the output file, enter one of the following values: </p> <p> <code>1:1</code>, <code>4:3</code>, <code>3:2</code>, <code>16:9</code> </p> <p> If you specify a value other than <code>auto</code>, Elastic Transcoder disables automatic detection of the aspect ratio. </p>"""
    interlaced: NotRequired["aws_sdk_elastic_transcoder.types.interlaced.Interlaced"]
    """<p>Whether the input file is interlaced. If you want Elastic Transcoder to automatically detect whether the input file is interlaced, specify <code>auto</code>. If you want to specify whether the input file is interlaced, enter one of the following values:</p> <p> <code>true</code>, <code>false</code> </p> <p>If you specify a value other than <code>auto</code>, Elastic Transcoder disables automatic detection of interlacing.</p>"""
    container: NotRequired[
        "aws_sdk_elastic_transcoder.types.job_container.JobContainer"
    ]
    """<p>The container type for the input file. If you want Elastic Transcoder to automatically detect the container type of the input file, specify <code>auto</code>. If you want to specify the container type for the input file, enter one of the following values: </p> <p> <code>3gp</code>, <code>aac</code>, <code>asf</code>, <code>avi</code>, <code>divx</code>, <code>flv</code>, <code>m4a</code>, <code>mkv</code>, <code>mov</code>, <code>mp3</code>, <code>mp4</code>, <code>mpeg</code>, <code>mpeg-ps</code>, <code>mpeg-ts</code>, <code>mxf</code>, <code>ogg</code>, <code>vob</code>, <code>wav</code>, <code>webm</code> </p>"""
    encryption: NotRequired["aws_sdk_elastic_transcoder.types.encryption.Encryption"]
    """<p>The encryption settings, if any, that are used for decrypting your input files. If your input file is encrypted, you must specify the mode that Elastic Transcoder uses to decrypt your file.</p>"""
    time_span: NotRequired["aws_sdk_elastic_transcoder.types.time_span.TimeSpan"]
    """<p>Settings for clipping an input. Each input can have different clip settings.</p>"""
    input_captions: NotRequired[
        "aws_sdk_elastic_transcoder.types.input_captions.InputCaptions"
    ]
    """<p>You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:</p> <ul> <li> <p> <b>Embedded:</b> Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file.</p> <p>Valid input values include: <code>CEA-608 (EIA-608</code>, first non-empty channel only), <code>CEA-708 (EIA-708</code>, first non-empty channel only), and <code>mov-text</code> </p> <p>Valid outputs include: <code>mov-text</code> </p> <p>Elastic Transcoder supports a maximum of one embedded format per output.</p> </li> <li> <p> <b>Sidecar:</b> Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file.</p> <p>Valid input values include: <code>dfxp</code> (first div element only), <code>ebu-tt</code>, <code>scc</code>, <code>smpt</code>, <code>srt</code>, <code>ttml</code> (first div element only), and <code>webvtt</code> </p> <p>Valid outputs include: <code>dfxp</code> (first div element only), <code>scc</code>, <code>srt</code>, and <code>webvtt</code>.</p> </li> </ul> <p>If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.</p> <p>Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.</p> <p>To remove captions or leave the captions empty, set <code>Captions</code> to null. To pass through existing captions unchanged, set the <code>MergePolicy</code> to <code>MergeRetain</code>, and pass in a null <code>CaptionSources</code> array.</p> <p>For more information on embedded files, see the Subtitles Wikipedia page.</p> <p>For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.</p>"""
    detected_properties: NotRequired[
        "aws_sdk_elastic_transcoder.types.detected_properties.DetectedProperties"
    ]
    """<p>The detected properties of the input file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobInput) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "frame_rate" in value:
        out["FrameRate"] = value["frame_rate"]
    if "resolution" in value:
        out["Resolution"] = value["resolution"]
    if "aspect_ratio" in value:
        out["AspectRatio"] = value["aspect_ratio"]
    if "interlaced" in value:
        out["Interlaced"] = value["interlaced"]
    if "container" in value:
        out["Container"] = value["container"]
    if "encryption" in value:
        import aws_sdk_elastic_transcoder.types.encryption

        out["Encryption"] = aws_sdk_elastic_transcoder.types.encryption.serialize_json(
            value["encryption"]
        )
    if "time_span" in value:
        import aws_sdk_elastic_transcoder.types.time_span

        out["TimeSpan"] = aws_sdk_elastic_transcoder.types.time_span.serialize_json(
            value["time_span"]
        )
    if "input_captions" in value:
        import aws_sdk_elastic_transcoder.types.input_captions

        out["InputCaptions"] = (
            aws_sdk_elastic_transcoder.types.input_captions.serialize_json(
                value["input_captions"]
            )
        )
    if "detected_properties" in value:
        import aws_sdk_elastic_transcoder.types.detected_properties

        out["DetectedProperties"] = (
            aws_sdk_elastic_transcoder.types.detected_properties.serialize_json(
                value["detected_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobInput:
    out: JobInput = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "FrameRate" in data:
        out["frame_rate"] = data["FrameRate"]
    if "Resolution" in data:
        out["resolution"] = data["Resolution"]
    if "AspectRatio" in data:
        out["aspect_ratio"] = data["AspectRatio"]
    if "Interlaced" in data:
        out["interlaced"] = data["Interlaced"]
    if "Container" in data:
        out["container"] = data["Container"]
    if "Encryption" in data:
        import aws_sdk_elastic_transcoder.types.encryption

        out["encryption"] = (
            aws_sdk_elastic_transcoder.types.encryption.deserialize_json(
                data["Encryption"]
            )
        )
    if "TimeSpan" in data:
        import aws_sdk_elastic_transcoder.types.time_span

        out["time_span"] = aws_sdk_elastic_transcoder.types.time_span.deserialize_json(
            data["TimeSpan"]
        )
    if "InputCaptions" in data:
        import aws_sdk_elastic_transcoder.types.input_captions

        out["input_captions"] = (
            aws_sdk_elastic_transcoder.types.input_captions.deserialize_json(
                data["InputCaptions"]
            )
        )
    if "DetectedProperties" in data:
        import aws_sdk_elastic_transcoder.types.detected_properties

        out["detected_properties"] = (
            aws_sdk_elastic_transcoder.types.detected_properties.deserialize_json(
                data["DetectedProperties"]
            )
        )
    return out
