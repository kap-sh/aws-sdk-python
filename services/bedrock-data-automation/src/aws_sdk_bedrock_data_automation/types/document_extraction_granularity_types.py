"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DocumentExtractionGranularityTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.document_extraction_granularity_type

DocumentExtractionGranularityTypes: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.document_extraction_granularity_type.DocumentExtractionGranularityType"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentExtractionGranularityTypes) -> list:
    import aws_sdk_bedrock_data_automation.types.document_extraction_granularity_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.document_extraction_granularity_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DocumentExtractionGranularityTypes:
    import aws_sdk_bedrock_data_automation.types.document_extraction_granularity_type

    out: DocumentExtractionGranularityTypes = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.document_extraction_granularity_type.deserialize_json(
                item
            )
        )
    return out
