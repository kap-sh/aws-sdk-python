"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoStandardOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.video_standard_extraction
    import aws_sdk_bedrock_data_automation.types.video_standard_generative_field


class VideoStandardOutputConfiguration(TypedDict):
    extraction: NotRequired[
        "aws_sdk_bedrock_data_automation.types.video_standard_extraction.VideoStandardExtraction"
    ]
    generative_field: NotRequired[
        "aws_sdk_bedrock_data_automation.types.video_standard_generative_field.VideoStandardGenerativeField"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VideoStandardOutputConfiguration) -> dict:
    out: dict = {}
    if "extraction" in value:
        import aws_sdk_bedrock_data_automation.types.video_standard_extraction

        out["extraction"] = (
            aws_sdk_bedrock_data_automation.types.video_standard_extraction.serialize_json(
                value["extraction"]
            )
        )
    if "generative_field" in value:
        import aws_sdk_bedrock_data_automation.types.video_standard_generative_field

        out["generativeField"] = (
            aws_sdk_bedrock_data_automation.types.video_standard_generative_field.serialize_json(
                value["generative_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoStandardOutputConfiguration:
    out: VideoStandardOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "extraction" in data:
        import aws_sdk_bedrock_data_automation.types.video_standard_extraction

        out["extraction"] = (
            aws_sdk_bedrock_data_automation.types.video_standard_extraction.deserialize_json(
                data["extraction"]
            )
        )
    if "generativeField" in data:
        import aws_sdk_bedrock_data_automation.types.video_standard_generative_field

        out["generative_field"] = (
            aws_sdk_bedrock_data_automation.types.video_standard_generative_field.deserialize_json(
                data["generativeField"]
            )
        )
    return out
