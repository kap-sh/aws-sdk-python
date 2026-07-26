"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAutomationStepExecutionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.step_execution_list


class DescribeAutomationStepExecutionsResult(TypedDict, closed=True):
    step_executions: NotRequired["capo_ssm.types.step_execution_list.StepExecutionList"]
    """<p>A list of details about the current state of all steps that make up an execution.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutomationStepExecutionsResult) -> dict:
    out: dict = {}
    if "step_executions" in value:
        import capo_ssm.types.step_execution_list

        out["StepExecutions"] = (
            capo_ssm.types.step_execution_list.serialize_aws_json_1_1(
                value["step_executions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutomationStepExecutionsResult:
    out: DescribeAutomationStepExecutionsResult = {}  # type: ignore[typeddict-item]
    if "StepExecutions" in data:
        import capo_ssm.types.step_execution_list

        out["step_executions"] = (
            capo_ssm.types.step_execution_list.deserialize_aws_json_1_1(
                data["StepExecutions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
