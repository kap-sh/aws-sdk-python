"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#StandardOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.audio_standard_output_configuration
    import aws_sdk_bedrock_data_automation.types.document_standard_output_configuration
    import aws_sdk_bedrock_data_automation.types.image_standard_output_configuration
    import aws_sdk_bedrock_data_automation.types.video_standard_output_configuration


class StandardOutputConfiguration(TypedDict):
    document: NotRequired[
        "aws_sdk_bedrock_data_automation.types.document_standard_output_configuration.DocumentStandardOutputConfiguration"
    ]
    image: NotRequired[
        "aws_sdk_bedrock_data_automation.types.image_standard_output_configuration.ImageStandardOutputConfiguration"
    ]
    video: NotRequired[
        "aws_sdk_bedrock_data_automation.types.video_standard_output_configuration.VideoStandardOutputConfiguration"
    ]
    audio: NotRequired[
        "aws_sdk_bedrock_data_automation.types.audio_standard_output_configuration.AudioStandardOutputConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StandardOutputConfiguration) -> dict:
    out: dict = {}
    if "document" in value:
        import aws_sdk_bedrock_data_automation.types.document_standard_output_configuration

        out["document"] = (
            aws_sdk_bedrock_data_automation.types.document_standard_output_configuration.serialize_json(
                value["document"]
            )
        )
    if "image" in value:
        import aws_sdk_bedrock_data_automation.types.image_standard_output_configuration

        out["image"] = (
            aws_sdk_bedrock_data_automation.types.image_standard_output_configuration.serialize_json(
                value["image"]
            )
        )
    if "video" in value:
        import aws_sdk_bedrock_data_automation.types.video_standard_output_configuration

        out["video"] = (
            aws_sdk_bedrock_data_automation.types.video_standard_output_configuration.serialize_json(
                value["video"]
            )
        )
    if "audio" in value:
        import aws_sdk_bedrock_data_automation.types.audio_standard_output_configuration

        out["audio"] = (
            aws_sdk_bedrock_data_automation.types.audio_standard_output_configuration.serialize_json(
                value["audio"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardOutputConfiguration:
    out: StandardOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "document" in data:
        import aws_sdk_bedrock_data_automation.types.document_standard_output_configuration

        out["document"] = (
            aws_sdk_bedrock_data_automation.types.document_standard_output_configuration.deserialize_json(
                data["document"]
            )
        )
    if "image" in data:
        import aws_sdk_bedrock_data_automation.types.image_standard_output_configuration

        out["image"] = (
            aws_sdk_bedrock_data_automation.types.image_standard_output_configuration.deserialize_json(
                data["image"]
            )
        )
    if "video" in data:
        import aws_sdk_bedrock_data_automation.types.video_standard_output_configuration

        out["video"] = (
            aws_sdk_bedrock_data_automation.types.video_standard_output_configuration.deserialize_json(
                data["video"]
            )
        )
    if "audio" in data:
        import aws_sdk_bedrock_data_automation.types.audio_standard_output_configuration

        out["audio"] = (
            aws_sdk_bedrock_data_automation.types.audio_standard_output_configuration.deserialize_json(
                data["audio"]
            )
        )
    return out
