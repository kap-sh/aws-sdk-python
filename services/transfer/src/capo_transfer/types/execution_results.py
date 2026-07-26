"""Generated from Smithy shape ``com.amazonaws.transfer#ExecutionResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.execution_step_results


class ExecutionResults(TypedDict, closed=True):
    steps: NotRequired[
        "capo_transfer.types.execution_step_results.ExecutionStepResults"
    ]
    """<p>Specifies the details for the steps that are in the specified workflow.</p>"""
    on_exception_steps: NotRequired[
        "capo_transfer.types.execution_step_results.ExecutionStepResults"
    ]
    """<p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionResults) -> dict:
    out: dict = {}
    if "steps" in value:
        import capo_transfer.types.execution_step_results

        out["Steps"] = (
            capo_transfer.types.execution_step_results.serialize_aws_json_1_1(
                value["steps"]
            )
        )
    if "on_exception_steps" in value:
        import capo_transfer.types.execution_step_results

        out["OnExceptionSteps"] = (
            capo_transfer.types.execution_step_results.serialize_aws_json_1_1(
                value["on_exception_steps"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionResults:
    out: ExecutionResults = {}  # type: ignore[typeddict-item]
    if "Steps" in data:
        import capo_transfer.types.execution_step_results

        out["steps"] = (
            capo_transfer.types.execution_step_results.deserialize_aws_json_1_1(
                data["Steps"]
            )
        )
    if "OnExceptionSteps" in data:
        import capo_transfer.types.execution_step_results

        out["on_exception_steps"] = (
            capo_transfer.types.execution_step_results.deserialize_aws_json_1_1(
                data["OnExceptionSteps"]
            )
        )
    return out
