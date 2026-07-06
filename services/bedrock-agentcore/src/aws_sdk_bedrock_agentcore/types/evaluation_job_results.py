"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationJobResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluator_summary_list


class EvaluationJobResults(TypedDict, closed=True):
    number_of_sessions_completed: NotRequired["int"]
    """<p>The number of sessions that have been successfully evaluated.</p>"""
    number_of_sessions_in_progress: NotRequired["int"]
    """<p>The number of sessions currently being evaluated.</p>"""
    number_of_sessions_failed: NotRequired["int"]
    """<p>The number of sessions that failed evaluation.</p>"""
    total_number_of_sessions: NotRequired["int"]
    """<p>The total number of sessions included in the batch evaluation.</p>"""
    number_of_sessions_ignored: NotRequired["int"]
    """<p>The number of sessions that were ignored during evaluation.</p>"""
    evaluator_summaries: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluator_summary_list.EvaluatorSummaryList"
    ]
    """<p>A list of per-evaluator summary statistics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationJobResults) -> dict:
    out: dict = {}
    if "number_of_sessions_completed" in value:
        out["numberOfSessionsCompleted"] = value["number_of_sessions_completed"]
    if "number_of_sessions_in_progress" in value:
        out["numberOfSessionsInProgress"] = value["number_of_sessions_in_progress"]
    if "number_of_sessions_failed" in value:
        out["numberOfSessionsFailed"] = value["number_of_sessions_failed"]
    if "total_number_of_sessions" in value:
        out["totalNumberOfSessions"] = value["total_number_of_sessions"]
    if "number_of_sessions_ignored" in value:
        out["numberOfSessionsIgnored"] = value["number_of_sessions_ignored"]
    if "evaluator_summaries" in value:
        import aws_sdk_bedrock_agentcore.types.evaluator_summary_list

        out["evaluatorSummaries"] = (
            aws_sdk_bedrock_agentcore.types.evaluator_summary_list.serialize_json(
                value["evaluator_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationJobResults:
    out: EvaluationJobResults = {}  # type: ignore[typeddict-item]
    if "numberOfSessionsCompleted" in data:
        out["number_of_sessions_completed"] = data["numberOfSessionsCompleted"]
    if "numberOfSessionsInProgress" in data:
        out["number_of_sessions_in_progress"] = data["numberOfSessionsInProgress"]
    if "numberOfSessionsFailed" in data:
        out["number_of_sessions_failed"] = data["numberOfSessionsFailed"]
    if "totalNumberOfSessions" in data:
        out["total_number_of_sessions"] = data["totalNumberOfSessions"]
    if "numberOfSessionsIgnored" in data:
        out["number_of_sessions_ignored"] = data["numberOfSessionsIgnored"]
    if "evaluatorSummaries" in data:
        import aws_sdk_bedrock_agentcore.types.evaluator_summary_list

        out["evaluator_summaries"] = (
            aws_sdk_bedrock_agentcore.types.evaluator_summary_list.deserialize_json(
                data["evaluatorSummaries"]
            )
        )
    return out
