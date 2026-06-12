"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioExtractionCategoryTypeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.transcript_configuration


class AudioExtractionCategoryTypeConfiguration(TypedDict):
    transcript: NotRequired[
        "aws_sdk_bedrock_data_automation.types.transcript_configuration.TranscriptConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionCategoryTypeConfiguration) -> dict:
    out: dict = {}
    if "transcript" in value:
        import aws_sdk_bedrock_data_automation.types.transcript_configuration

        out["transcript"] = (
            aws_sdk_bedrock_data_automation.types.transcript_configuration.serialize_json(
                value["transcript"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioExtractionCategoryTypeConfiguration:
    out: AudioExtractionCategoryTypeConfiguration = {}  # type: ignore[typeddict-item]
    if "transcript" in data:
        import aws_sdk_bedrock_data_automation.types.transcript_configuration

        out["transcript"] = (
            aws_sdk_bedrock_data_automation.types.transcript_configuration.deserialize_json(
                data["transcript"]
            )
        )
    return out
