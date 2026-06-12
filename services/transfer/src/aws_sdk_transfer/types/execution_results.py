"""Generated from Smithy shape ``com.amazonaws.transfer#ExecutionResults``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.execution_step_results


class ExecutionResults(TypedDict):
    steps: NotRequired[
        "aws_sdk_transfer.types.execution_step_results.ExecutionStepResults"
    ]
    """<p>Specifies the details for the steps that are in the specified workflow.</p>"""
    on_exception_steps: NotRequired[
        "aws_sdk_transfer.types.execution_step_results.ExecutionStepResults"
    ]
    """<p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionResults) -> dict:
    out: dict = {}
    if "steps" in value:
        import aws_sdk_transfer.types.execution_step_results

        out["Steps"] = (
            aws_sdk_transfer.types.execution_step_results.serialize_aws_json_1_1(
                value["steps"]
            )
        )
    if "on_exception_steps" in value:
        import aws_sdk_transfer.types.execution_step_results

        out["OnExceptionSteps"] = (
            aws_sdk_transfer.types.execution_step_results.serialize_aws_json_1_1(
                value["on_exception_steps"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionResults:
    out: ExecutionResults = {}  # type: ignore[typeddict-item]
    if "Steps" in data:
        import aws_sdk_transfer.types.execution_step_results

        out["steps"] = (
            aws_sdk_transfer.types.execution_step_results.deserialize_aws_json_1_1(
                data["Steps"]
            )
        )
    if "OnExceptionSteps" in data:
        import aws_sdk_transfer.types.execution_step_results

        out["on_exception_steps"] = (
            aws_sdk_transfer.types.execution_step_results.deserialize_aws_json_1_1(
                data["OnExceptionSteps"]
            )
        )
    return out
