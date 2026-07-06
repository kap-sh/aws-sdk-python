"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoStandardExtraction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.video_bounding_box
    import aws_sdk_bedrock_data_automation.types.video_extraction_category


class VideoStandardExtraction(TypedDict, closed=True):
    category: "aws_sdk_bedrock_data_automation.types.video_extraction_category.VideoExtractionCategory"
    bounding_box: (
        "aws_sdk_bedrock_data_automation.types.video_bounding_box.VideoBoundingBox"
    )


# --- restJson1 ser/de ---
def serialize_json(value: VideoStandardExtraction) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.video_extraction_category

    out["category"] = (
        aws_sdk_bedrock_data_automation.types.video_extraction_category.serialize_json(
            value["category"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.video_bounding_box

    out["boundingBox"] = (
        aws_sdk_bedrock_data_automation.types.video_bounding_box.serialize_json(
            value["bounding_box"]
        )
    )
    return out


def deserialize_json(data: dict) -> VideoStandardExtraction:
    out: VideoStandardExtraction = {}  # type: ignore[typeddict-item]
    if "category" in data:
        import aws_sdk_bedrock_data_automation.types.video_extraction_category

        out["category"] = (
            aws_sdk_bedrock_data_automation.types.video_extraction_category.deserialize_json(
                data["category"]
            )
        )
    else:
        raise DeserializationError("VideoStandardExtraction.category required")
    if "boundingBox" in data:
        import aws_sdk_bedrock_data_automation.types.video_bounding_box

        out["bounding_box"] = (
            aws_sdk_bedrock_data_automation.types.video_bounding_box.deserialize_json(
                data["boundingBox"]
            )
        )
    else:
        raise DeserializationError("VideoStandardExtraction.bounding_box required")
    return out
