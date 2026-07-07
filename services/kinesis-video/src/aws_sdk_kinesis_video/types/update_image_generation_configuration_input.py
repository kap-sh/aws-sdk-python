"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateImageGenerationConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.image_generation_configuration
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name


class UpdateImageGenerationConfigurationInput(TypedDict, closed=True):
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream from which to update the image generation configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to update the image generation configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>"""
    image_generation_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.image_generation_configuration.ImageGenerationConfiguration"
    ]
    """<p>The structure that contains the information required for the KVS images delivery. If the structure is null, the configuration will be deleted from the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateImageGenerationConfigurationInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "image_generation_configuration" in value:
        import aws_sdk_kinesis_video.types.image_generation_configuration

        out["ImageGenerationConfiguration"] = (
            aws_sdk_kinesis_video.types.image_generation_configuration.serialize_json(
                value["image_generation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateImageGenerationConfigurationInput:
    out: UpdateImageGenerationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "ImageGenerationConfiguration" in data:
        import aws_sdk_kinesis_video.types.image_generation_configuration

        out["image_generation_configuration"] = (
            aws_sdk_kinesis_video.types.image_generation_configuration.deserialize_json(
                data["ImageGenerationConfiguration"]
            )
        )
    return out
