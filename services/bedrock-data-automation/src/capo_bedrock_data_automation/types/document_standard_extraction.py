"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentStandardExtraction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.document_bounding_box
    import capo_bedrock_data_automation.types.document_extraction_granularity


class DocumentStandardExtraction(TypedDict, closed=True):
    granularity: "capo_bedrock_data_automation.types.document_extraction_granularity.DocumentExtractionGranularity"
    bounding_box: (
        "capo_bedrock_data_automation.types.document_bounding_box.DocumentBoundingBox"
    )


# --- restJson1 ser/de ---
def serialize_json(value: DocumentStandardExtraction) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.document_extraction_granularity

    out["granularity"] = (
        capo_bedrock_data_automation.types.document_extraction_granularity.serialize_json(
            value["granularity"]
        )
    )
    import capo_bedrock_data_automation.types.document_bounding_box

    out["boundingBox"] = (
        capo_bedrock_data_automation.types.document_bounding_box.serialize_json(
            value["bounding_box"]
        )
    )
    return out


def deserialize_json(data: dict) -> DocumentStandardExtraction:
    out: DocumentStandardExtraction = {}  # type: ignore[typeddict-item]
    if data.get("granularity") is not None:
        import capo_bedrock_data_automation.types.document_extraction_granularity

        out["granularity"] = (
            capo_bedrock_data_automation.types.document_extraction_granularity.deserialize_json(
                data["granularity"]
            )
        )
    else:
        raise DeserializationError("DocumentStandardExtraction.granularity required")
    if data.get("boundingBox") is not None:
        import capo_bedrock_data_automation.types.document_bounding_box

        out["bounding_box"] = (
            capo_bedrock_data_automation.types.document_bounding_box.deserialize_json(
                data["boundingBox"]
            )
        )
    else:
        raise DeserializationError("DocumentStandardExtraction.bounding_box required")
    return out
