"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartMemoryExtractionJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.extraction_job
    import capo_bedrock_agentcore.types.memory_id


class StartMemoryExtractionJobInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory for which to start extraction jobs.</p>"""
    extraction_job: "capo_bedrock_agentcore.types.extraction_job.ExtractionJob"
    """<p>Extraction job to start in this operation.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMemoryExtractionJobInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.extraction_job

    out["extractionJob"] = capo_bedrock_agentcore.types.extraction_job.serialize_json(
        value["extraction_job"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartMemoryExtractionJobInput:
    out: StartMemoryExtractionJobInput = {}  # type: ignore[typeddict-item]
    if "extractionJob" in data:
        import capo_bedrock_agentcore.types.extraction_job

        out["extraction_job"] = (
            capo_bedrock_agentcore.types.extraction_job.deserialize_json(
                data["extractionJob"]
            )
        )
    else:
        raise DeserializationError(
            "StartMemoryExtractionJobInput.extraction_job required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
