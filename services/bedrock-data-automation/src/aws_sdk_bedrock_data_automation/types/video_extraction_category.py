"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoExtractionCategory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.state
    import aws_sdk_bedrock_data_automation.types.video_extraction_category_types


class VideoExtractionCategory(TypedDict):
    state: "aws_sdk_bedrock_data_automation.types.state.State"
    types: NotRequired[
        "aws_sdk_bedrock_data_automation.types.video_extraction_category_types.VideoExtractionCategoryTypes"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionCategory) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.state

    out["state"] = aws_sdk_bedrock_data_automation.types.state.serialize_json(
        value["state"]
    )
    if "types" in value:
        import aws_sdk_bedrock_data_automation.types.video_extraction_category_types

        out["types"] = (
            aws_sdk_bedrock_data_automation.types.video_extraction_category_types.serialize_json(
                value["types"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoExtractionCategory:
    out: VideoExtractionCategory = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_bedrock_data_automation.types.state

        out["state"] = aws_sdk_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("VideoExtractionCategory.state required")
    if "types" in data:
        import aws_sdk_bedrock_data_automation.types.video_extraction_category_types

        out["types"] = (
            aws_sdk_bedrock_data_automation.types.video_extraction_category_types.deserialize_json(
                data["types"]
            )
        )
    return out
