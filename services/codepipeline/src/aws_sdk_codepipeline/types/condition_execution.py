"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.condition_execution_status
    import aws_sdk_codepipeline.types.execution_summary
    import aws_sdk_codepipeline.types.timestamp


class ConditionExecution(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_codepipeline.types.condition_execution_status.ConditionExecutionStatus"
    ]
    """<p>The status of the run for a condition.</p>"""
    summary: NotRequired[
        "aws_sdk_codepipeline.types.execution_summary.ExecutionSummary"
    ]
    """<p>The summary of information about a run for a condition.</p>"""
    last_status_change: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The last status change of the condition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionExecution) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_codepipeline.types.condition_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.condition_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    if "last_status_change" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["lastStatusChange"] = (
            aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_status_change"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionExecution:
    out: ConditionExecution = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_codepipeline.types.condition_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.condition_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "summary" in data:
        out["summary"] = data["summary"]
    if "lastStatusChange" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["last_status_change"] = (
            aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastStatusChange"]
            )
        )
    return out
