"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluator_statistics


class EvaluatorSummary(TypedDict, closed=True):
    evaluator_id: NotRequired["str"]
    """<p>The unique identifier of the evaluator.</p>"""
    statistics: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluator_statistics.EvaluatorStatistics"
    ]
    """<p>The aggregated statistics for this evaluator.</p>"""
    total_evaluated: NotRequired["int"]
    """<p>The total number of sessions evaluated by this evaluator.</p>"""
    total_failed: NotRequired["int"]
    """<p>The total number of sessions that failed evaluation by this evaluator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorSummary) -> dict:
    out: dict = {}
    if "evaluator_id" in value:
        out["evaluatorId"] = value["evaluator_id"]
    if "statistics" in value:
        import aws_sdk_bedrock_agentcore.types.evaluator_statistics

        out["statistics"] = (
            aws_sdk_bedrock_agentcore.types.evaluator_statistics.serialize_json(
                value["statistics"]
            )
        )
    if "total_evaluated" in value:
        out["totalEvaluated"] = value["total_evaluated"]
    if "total_failed" in value:
        out["totalFailed"] = value["total_failed"]
    return out


def deserialize_json(data: dict) -> EvaluatorSummary:
    out: EvaluatorSummary = {}  # type: ignore[typeddict-item]
    if "evaluatorId" in data:
        out["evaluator_id"] = data["evaluatorId"]
    if "statistics" in data:
        import aws_sdk_bedrock_agentcore.types.evaluator_statistics

        out["statistics"] = (
            aws_sdk_bedrock_agentcore.types.evaluator_statistics.deserialize_json(
                data["statistics"]
            )
        )
    if "totalEvaluated" in data:
        out["total_evaluated"] = data["totalEvaluated"]
    if "totalFailed" in data:
        out["total_failed"] = data["totalFailed"]
    return out
