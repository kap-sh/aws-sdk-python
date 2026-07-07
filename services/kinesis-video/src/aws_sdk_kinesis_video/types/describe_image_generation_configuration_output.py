"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeImageGenerationConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.image_generation_configuration


class DescribeImageGenerationConfigurationOutput(TypedDict, closed=True):
    image_generation_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.image_generation_configuration.ImageGenerationConfiguration"
    ]
    """<p>The structure that contains the information required for the Kinesis video stream (KVS) images delivery. If this structure is null, the configuration will be deleted from the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeImageGenerationConfigurationOutput) -> dict:
    out: dict = {}
    if "image_generation_configuration" in value:
        import aws_sdk_kinesis_video.types.image_generation_configuration

        out["ImageGenerationConfiguration"] = (
            aws_sdk_kinesis_video.types.image_generation_configuration.serialize_json(
                value["image_generation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeImageGenerationConfigurationOutput:
    out: DescribeImageGenerationConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "ImageGenerationConfiguration" in data:
        import aws_sdk_kinesis_video.types.image_generation_configuration

        out["image_generation_configuration"] = (
            aws_sdk_kinesis_video.types.image_generation_configuration.deserialize_json(
                data["ImageGenerationConfiguration"]
            )
        )
    return out
