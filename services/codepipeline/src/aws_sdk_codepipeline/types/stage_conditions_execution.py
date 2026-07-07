"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageConditionsExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.condition_execution_status
    import aws_sdk_codepipeline.types.execution_summary


class StageConditionsExecution(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_codepipeline.types.condition_execution_status.ConditionExecutionStatus"
    ]
    """<p>The status of a run of a condition for a stage.</p>"""
    summary: NotRequired[
        "aws_sdk_codepipeline.types.execution_summary.ExecutionSummary"
    ]
    """<p>A summary of the run of the condition for a stage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageConditionsExecution) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> StageConditionsExecution:
    out: StageConditionsExecution = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_codepipeline.types.condition_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.condition_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "summary" in data:
        out["summary"] = data["summary"]
    return out
