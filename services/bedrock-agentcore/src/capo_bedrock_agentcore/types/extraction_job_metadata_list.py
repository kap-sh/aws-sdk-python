"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.extraction_job_metadata

ExtractionJobMetadataList: TypeAlias = list[
    "capo_bedrock_agentcore.types.extraction_job_metadata.ExtractionJobMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJobMetadataList) -> list:
    import capo_bedrock_agentcore.types.extraction_job_metadata

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.extraction_job_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExtractionJobMetadataList:
    import capo_bedrock_agentcore.types.extraction_job_metadata

    out: ExtractionJobMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.extraction_job_metadata.deserialize_json(item)
        )
    return out
