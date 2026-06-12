"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.ingestion_job_summary

IngestionJobSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.ingestion_job_summary.IngestionJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobSummaries) -> list:
    import aws_sdk_bedrock_agent.types.ingestion_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.ingestion_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IngestionJobSummaries:
    import aws_sdk_bedrock_agent.types.ingestion_job_summary

    out: IngestionJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.ingestion_job_summary.deserialize_json(item)
        )
    return out
