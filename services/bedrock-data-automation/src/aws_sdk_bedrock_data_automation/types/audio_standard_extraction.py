"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioStandardExtraction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.audio_extraction_category


class AudioStandardExtraction(TypedDict, closed=True):
    category: "aws_sdk_bedrock_data_automation.types.audio_extraction_category.AudioExtractionCategory"


# --- restJson1 ser/de ---
def serialize_json(value: AudioStandardExtraction) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.audio_extraction_category

    out["category"] = (
        aws_sdk_bedrock_data_automation.types.audio_extraction_category.serialize_json(
            value["category"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudioStandardExtraction:
    out: AudioStandardExtraction = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import aws_sdk_bedrock_data_automation.types.audio_extraction_category

        out["category"] = (
            aws_sdk_bedrock_data_automation.types.audio_extraction_category.deserialize_json(
                data["category"]
            )
        )
    else:
        raise DeserializationError("AudioStandardExtraction.category required")
    return out
