"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentExtractionGranularity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.document_extraction_granularity_types


class DocumentExtractionGranularity(TypedDict, closed=True):
    types: NotRequired[
        "capo_bedrock_data_automation.types.document_extraction_granularity_types.DocumentExtractionGranularityTypes"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentExtractionGranularity) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_bedrock_data_automation.types.document_extraction_granularity_types

        out["types"] = (
            capo_bedrock_data_automation.types.document_extraction_granularity_types.serialize_json(
                value["types"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentExtractionGranularity:
    out: DocumentExtractionGranularity = {}  # type: ignore[typeddict-item]
    if "types" in data:
        import capo_bedrock_data_automation.types.document_extraction_granularity_types

        out["types"] = (
            capo_bedrock_data_automation.types.document_extraction_granularity_types.deserialize_json(
                data["types"]
            )
        )
    return out
