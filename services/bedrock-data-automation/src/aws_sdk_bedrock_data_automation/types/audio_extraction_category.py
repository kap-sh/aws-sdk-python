"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioExtractionCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.audio_extraction_category_type_configuration
    import aws_sdk_bedrock_data_automation.types.audio_extraction_category_types
    import aws_sdk_bedrock_data_automation.types.state


class AudioExtractionCategory(TypedDict, closed=True):
    state: "aws_sdk_bedrock_data_automation.types.state.State"
    types: NotRequired[
        "aws_sdk_bedrock_data_automation.types.audio_extraction_category_types.AudioExtractionCategoryTypes"
    ]
    type_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.audio_extraction_category_type_configuration.AudioExtractionCategoryTypeConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionCategory) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.state

    out["state"] = aws_sdk_bedrock_data_automation.types.state.serialize_json(
        value["state"]
    )
    if "types" in value:
        import aws_sdk_bedrock_data_automation.types.audio_extraction_category_types

        out["types"] = (
            aws_sdk_bedrock_data_automation.types.audio_extraction_category_types.serialize_json(
                value["types"]
            )
        )
    if "type_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.audio_extraction_category_type_configuration

        out["typeConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.audio_extraction_category_type_configuration.serialize_json(
                value["type_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioExtractionCategory:
    out: AudioExtractionCategory = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_bedrock_data_automation.types.state

        out["state"] = aws_sdk_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("AudioExtractionCategory.state required")
    if "types" in data:
        import aws_sdk_bedrock_data_automation.types.audio_extraction_category_types

        out["types"] = (
            aws_sdk_bedrock_data_automation.types.audio_extraction_category_types.deserialize_json(
                data["types"]
            )
        )
    if "typeConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.audio_extraction_category_type_configuration

        out["type_configuration"] = (
            aws_sdk_bedrock_data_automation.types.audio_extraction_category_type_configuration.deserialize_json(
                data["typeConfiguration"]
            )
        )
    return out
