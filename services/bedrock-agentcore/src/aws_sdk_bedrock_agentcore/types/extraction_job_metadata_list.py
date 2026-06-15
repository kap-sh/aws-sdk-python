"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.extraction_job_metadata

ExtractionJobMetadataList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.extraction_job_metadata.ExtractionJobMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJobMetadataList) -> list:
    import aws_sdk_bedrock_agentcore.types.extraction_job_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.extraction_job_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExtractionJobMetadataList:
    import aws_sdk_bedrock_agentcore.types.extraction_job_metadata

    out: ExtractionJobMetadataList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.extraction_job_metadata.deserialize_json(
                item
            )
        )
    return out
