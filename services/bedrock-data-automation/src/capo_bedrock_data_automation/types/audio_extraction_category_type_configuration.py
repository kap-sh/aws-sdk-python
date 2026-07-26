"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioExtractionCategoryTypeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.transcript_configuration


class AudioExtractionCategoryTypeConfiguration(TypedDict, closed=True):
    transcript: NotRequired[
        "capo_bedrock_data_automation.types.transcript_configuration.TranscriptConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionCategoryTypeConfiguration) -> dict:
    out: dict = {}
    if "transcript" in value:
        import capo_bedrock_data_automation.types.transcript_configuration

        out["transcript"] = (
            capo_bedrock_data_automation.types.transcript_configuration.serialize_json(
                value["transcript"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioExtractionCategoryTypeConfiguration:
    out: AudioExtractionCategoryTypeConfiguration = {}  # type: ignore[typeddict-item]
    if "transcript" in data:
        import capo_bedrock_data_automation.types.transcript_configuration

        out["transcript"] = (
            capo_bedrock_data_automation.types.transcript_configuration.deserialize_json(
                data["transcript"]
            )
        )
    return out
