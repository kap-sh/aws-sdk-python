"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.ingestion_job_filter

IngestionJobFilters: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.ingestion_job_filter.IngestionJobFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobFilters) -> list:
    import aws_sdk_bedrock_agent.types.ingestion_job_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.ingestion_job_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IngestionJobFilters:
    import aws_sdk_bedrock_agent.types.ingestion_job_filter

    out: IngestionJobFilters = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.ingestion_job_filter.deserialize_json(item)
        )
    return out
