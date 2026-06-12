"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetIngestionJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.ingestion_job


class GetIngestionJobResponse(TypedDict):
    ingestion_job: "aws_sdk_bedrock_agent.types.ingestion_job.IngestionJob"
    """<p>Contains details about the data ingestion job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestionJobResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.ingestion_job

    out["ingestionJob"] = aws_sdk_bedrock_agent.types.ingestion_job.serialize_json(
        value["ingestion_job"]
    )
    return out


def deserialize_json(data: dict) -> GetIngestionJobResponse:
    out: GetIngestionJobResponse = {}  # type: ignore[typeddict-item]
    if "ingestionJob" in data:
        import aws_sdk_bedrock_agent.types.ingestion_job

        out["ingestion_job"] = (
            aws_sdk_bedrock_agent.types.ingestion_job.deserialize_json(
                data["ingestionJob"]
            )
        )
    else:
        raise DeserializationError("GetIngestionJobResponse.ingestion_job required")
    return out
