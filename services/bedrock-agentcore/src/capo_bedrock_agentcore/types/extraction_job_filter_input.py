"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobFilterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.extraction_job_status


class ExtractionJobFilterInput(TypedDict, closed=True):
    strategy_id: NotRequired["str"]
    """<p>The memory strategy identifier to filter extraction jobs by. If specified, only extraction jobs with this strategy ID are returned.</p>"""
    session_id: NotRequired["str"]
    """<p>The unique identifier of the session. If specified, only extraction jobs with this session ID are returned.</p>"""
    actor_id: NotRequired["str"]
    """<p>The identifier of the actor. If specified, only extraction jobs with this actor ID are returned.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore.types.extraction_job_status.ExtractionJobStatus"
    ]
    """<p>The status of the extraction job. If specified, only extraction jobs with this status are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJobFilterInput) -> dict:
    out: dict = {}
    if "strategy_id" in value:
        out["strategyId"] = value["strategy_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    if "status" in value:
        import capo_bedrock_agentcore.types.extraction_job_status

        out["status"] = (
            capo_bedrock_agentcore.types.extraction_job_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExtractionJobFilterInput:
    out: ExtractionJobFilterInput = {}  # type: ignore[typeddict-item]
    if data.get("strategyId") is not None:
        out["strategy_id"] = data["strategyId"]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.extraction_job_status

        out["status"] = (
            capo_bedrock_agentcore.types.extraction_job_status.deserialize_json(
                data["status"]
            )
        )
    return out
