"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetImagesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.format
    import aws_sdk_kinesis_video_archived_media.types.format_config
    import aws_sdk_kinesis_video_archived_media.types.get_images_max_results
    import aws_sdk_kinesis_video_archived_media.types.height_pixels
    import aws_sdk_kinesis_video_archived_media.types.image_selector_type
    import aws_sdk_kinesis_video_archived_media.types.next_token
    import aws_sdk_kinesis_video_archived_media.types.resource_arn
    import aws_sdk_kinesis_video_archived_media.types.sampling_interval
    import aws_sdk_kinesis_video_archived_media.types.stream_name
    import aws_sdk_kinesis_video_archived_media.types.timestamp
    import aws_sdk_kinesis_video_archived_media.types.width_pixels


class GetImagesInput(TypedDict):
    stream_name: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.stream_name.StreamName"
    ]
    """<p>The name of the stream from which to retrieve the images. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    stream_arn: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the stream from which to retrieve the images. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    image_selector_type: "aws_sdk_kinesis_video_archived_media.types.image_selector_type.ImageSelectorType"
    """<p>The origin of the Server or Producer timestamps to use to generate the images.</p>"""
    start_timestamp: "aws_sdk_kinesis_video_archived_media.types.timestamp.Timestamp"
    """<p>The starting point from which the images should be generated. This <code>StartTimestamp</code> must be within an inclusive range of timestamps for an image to be returned.</p>"""
    end_timestamp: "aws_sdk_kinesis_video_archived_media.types.timestamp.Timestamp"
    """<p>The end timestamp for the range of images to be generated. If the time range between <code>StartTimestamp</code> and <code>EndTimestamp</code> is more than 300 seconds above <code>StartTimestamp</code>, you will receive an <code>IllegalArgumentException</code>.</p>"""
    sampling_interval: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.sampling_interval.SamplingInterval"
    ]
    """<p>The time interval in milliseconds (ms) at which the images need to be generated from the stream. The minimum value that can be provided is 200 ms (5 images per second). If the timestamp range is less than the sampling interval, the image from the <code>startTimestamp</code> will be returned if available. </p>"""
    format: "aws_sdk_kinesis_video_archived_media.types.format.Format"
    """<p>The format that will be used to encode the image.</p>"""
    format_config: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.format_config.FormatConfig"
    ]
    """<p>The list of a key-value pair structure that contains extra parameters that can be applied when the image is generated. The <code>FormatConfig</code> key is the <code>JPEGQuality</code>, which indicates the JPEG quality key to be used to generate the image. The <code>FormatConfig</code> value accepts ints from 1 to 100. If the value is 1, the image will be generated with less quality and the best compression. If the value is 100, the image will be generated with the best quality and less compression. If no value is provided, the default value of the <code>JPEGQuality</code> key will be set to 80.</p>"""
    width_pixels: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.width_pixels.WidthPixels"
    ]
    """<p>The width of the output image that is used in conjunction with the <code>HeightPixels</code> parameter. When both <code>WidthPixels</code> and <code>HeightPixels</code> parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the <code>WidthPixels</code> parameter is provided or if only the <code>HeightPixels</code> is provided, a <code>ValidationException</code> will be thrown. If neither parameter is provided, the original image size from the stream will be returned.</p>"""
    height_pixels: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.height_pixels.HeightPixels"
    ]
    """<p>The height of the output image that is used in conjunction with the <code>WidthPixels</code> parameter. When both <code>HeightPixels</code> and <code>WidthPixels</code> parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the <code>HeightPixels</code> parameter is provided, its original aspect ratio will be used to calculate the <code>WidthPixels</code> ratio. If neither parameter is provided, the original image size will be returned.</p>"""
    max_results: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.get_images_max_results.GetImagesMaxResults"
    ]
    """<p>The maximum number of images to be returned by the API. </p> <note> <p>The default limit is 25 images per API response. Providing a <code>MaxResults</code> greater than this value will result in a page size of 25. Any additional results will be paginated. </p> </note>"""
    next_token: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.next_token.NextToken"
    ]
    """<p>A token that specifies where to start paginating the next set of Images. This is the <code>GetImages:NextToken</code> from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImagesInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import aws_sdk_kinesis_video_archived_media.types.image_selector_type

    out["ImageSelectorType"] = (
        aws_sdk_kinesis_video_archived_media.types.image_selector_type.serialize_json(
            value["image_selector_type"]
        )
    )
    import aws_sdk_kinesis_video_archived_media.types.timestamp

    out["StartTimestamp"] = (
        aws_sdk_kinesis_video_archived_media.types.timestamp.serialize_json(
            value["start_timestamp"]
        )
    )
    import aws_sdk_kinesis_video_archived_media.types.timestamp

    out["EndTimestamp"] = (
        aws_sdk_kinesis_video_archived_media.types.timestamp.serialize_json(
            value["end_timestamp"]
        )
    )
    if "sampling_interval" in value:
        out["SamplingInterval"] = value["sampling_interval"]
    import aws_sdk_kinesis_video_archived_media.types.format

    out["Format"] = aws_sdk_kinesis_video_archived_media.types.format.serialize_json(
        value["format"]
    )
    if "format_config" in value:
        import aws_sdk_kinesis_video_archived_media.types.format_config

        out["FormatConfig"] = (
            aws_sdk_kinesis_video_archived_media.types.format_config.serialize_json(
                value["format_config"]
            )
        )
    if "width_pixels" in value:
        out["WidthPixels"] = value["width_pixels"]
    if "height_pixels" in value:
        out["HeightPixels"] = value["height_pixels"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetImagesInput:
    out: GetImagesInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "ImageSelectorType" in data:
        import aws_sdk_kinesis_video_archived_media.types.image_selector_type

        out["image_selector_type"] = (
            aws_sdk_kinesis_video_archived_media.types.image_selector_type.deserialize_json(
                data["ImageSelectorType"]
            )
        )
    else:
        raise DeserializationError("GetImagesInput.image_selector_type required")
    if "StartTimestamp" in data:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["start_timestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    else:
        raise DeserializationError("GetImagesInput.start_timestamp required")
    if "EndTimestamp" in data:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["end_timestamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    else:
        raise DeserializationError("GetImagesInput.end_timestamp required")
    if "SamplingInterval" in data:
        out["sampling_interval"] = data["SamplingInterval"]
    if "Format" in data:
        import aws_sdk_kinesis_video_archived_media.types.format

        out["format"] = (
            aws_sdk_kinesis_video_archived_media.types.format.deserialize_json(
                data["Format"]
            )
        )
    else:
        raise DeserializationError("GetImagesInput.format required")
    if "FormatConfig" in data:
        import aws_sdk_kinesis_video_archived_media.types.format_config

        out["format_config"] = (
            aws_sdk_kinesis_video_archived_media.types.format_config.deserialize_json(
                data["FormatConfig"]
            )
        )
    if "WidthPixels" in data:
        out["width_pixels"] = data["WidthPixels"]
    if "HeightPixels" in data:
        out["height_pixels"] = data["HeightPixels"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
