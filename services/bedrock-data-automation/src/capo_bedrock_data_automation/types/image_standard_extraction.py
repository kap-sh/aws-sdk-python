"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageStandardExtraction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.image_bounding_box
    import capo_bedrock_data_automation.types.image_extraction_category


class ImageStandardExtraction(TypedDict, closed=True):
    category: "capo_bedrock_data_automation.types.image_extraction_category.ImageExtractionCategory"
    bounding_box: (
        "capo_bedrock_data_automation.types.image_bounding_box.ImageBoundingBox"
    )


# --- restJson1 ser/de ---
def serialize_json(value: ImageStandardExtraction) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.image_extraction_category

    out["category"] = (
        capo_bedrock_data_automation.types.image_extraction_category.serialize_json(
            value["category"]
        )
    )
    import capo_bedrock_data_automation.types.image_bounding_box

    out["boundingBox"] = (
        capo_bedrock_data_automation.types.image_bounding_box.serialize_json(
            value["bounding_box"]
        )
    )
    return out


def deserialize_json(data: dict) -> ImageStandardExtraction:
    out: ImageStandardExtraction = {}  # type: ignore[typeddict-item]
    if data.get("category") is not None:
        import capo_bedrock_data_automation.types.image_extraction_category

        out["category"] = (
            capo_bedrock_data_automation.types.image_extraction_category.deserialize_json(
                data["category"]
            )
        )
    else:
        raise DeserializationError("ImageStandardExtraction.category required")
    if data.get("boundingBox") is not None:
        import capo_bedrock_data_automation.types.image_bounding_box

        out["bounding_box"] = (
            capo_bedrock_data_automation.types.image_bounding_box.deserialize_json(
                data["boundingBox"]
            )
        )
    else:
        raise DeserializationError("ImageStandardExtraction.bounding_box required")
    return out
