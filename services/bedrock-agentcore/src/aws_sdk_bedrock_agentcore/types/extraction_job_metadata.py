"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionJobMetadata``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.extraction_job_messages
    import aws_sdk_bedrock_agentcore.types.extraction_job_status

class ExtractionJobMetadata(TypedDict):
    job_id: "str"
    """<p>The unique identifier for the extraction job.</p>"""
    messages: "aws_sdk_bedrock_agentcore.types.extraction_job_messages.ExtractionJobMessages"
    """<p>The messages associated with the extraction job.</p>"""
    status: NotRequired["aws_sdk_bedrock_agentcore.types.extraction_job_status.ExtractionJobStatus"]
    """<p>The current status of the extraction job.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The cause of failure, if the job did not complete successfully.</p>"""
    strategy_id: NotRequired["str"]
    """<p>The identifier of the memory strategy for this extraction job.</p>"""
    session_id: NotRequired["str"]
    """<p>The identifier of the session for this extraction job.</p>"""
    actor_id: NotRequired["str"]
    """<p>The identifier of the actor for this extraction job.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ExtractionJobMetadata) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    import aws_sdk_bedrock_agentcore.types.extraction_job_messages
    out["messages"] = aws_sdk_bedrock_agentcore.types.extraction_job_messages.serialize_json(value["messages"])
    if "status" in value:
        import aws_sdk_bedrock_agentcore.types.extraction_job_status
        out["status"] = aws_sdk_bedrock_agentcore.types.extraction_job_status.serialize_json(value["status"])
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "strategy_id" in value:
        out["strategyId"] = value["strategy_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    return out


def deserialize_json(data: dict) -> ExtractionJobMetadata:
    out: ExtractionJobMetadata = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    else:
        raise DeserializationError("ExtractionJobMetadata.job_id required")
    if "messages" in data:
        import aws_sdk_bedrock_agentcore.types.extraction_job_messages
        out["messages"] = aws_sdk_bedrock_agentcore.types.extraction_job_messages.deserialize_json(data["messages"])
    else:
        raise DeserializationError("ExtractionJobMetadata.messages required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.extraction_job_status
        out["status"] = aws_sdk_bedrock_agentcore.types.extraction_job_status.deserialize_json(data["status"])
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "strategyId" in data:
        out["strategy_id"] = data["strategyId"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "actorId" in data:
        out["actor_id"] = data["actorId"]
    return out