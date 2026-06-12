"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.ingestion_job_filter_value

IngestionJobFilterValues: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.ingestion_job_filter_value.IngestionJobFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> IngestionJobFilterValues:
    return list(data)
