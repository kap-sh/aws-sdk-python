"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAutomationStepExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_execution_id
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.step_execution_filter_list


class DescribeAutomationStepExecutionsRequest(TypedDict):
    automation_execution_id: (
        "aws_sdk_ssm.types.automation_execution_id.AutomationExecutionId"
    )
    """<p>The Automation execution ID for which you want step execution descriptions.</p>"""
    filters: NotRequired[
        "aws_sdk_ssm.types.step_execution_filter_list.StepExecutionFilterList"
    ]
    """<p>One or more filters to limit the number of step executions returned by the request.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    reverse_order: NotRequired["aws_sdk_ssm.types.boolean.Boolean"]
    """<p>Indicates whether to list step executions in reverse order by start time. The default value is 'false'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutomationStepExecutionsRequest) -> dict:
    out: dict = {}
    out["AutomationExecutionId"] = value["automation_execution_id"]
    if "filters" in value:
        import aws_sdk_ssm.types.step_execution_filter_list

        out["Filters"] = (
            aws_sdk_ssm.types.step_execution_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "reverse_order" in value:
        out["ReverseOrder"] = value["reverse_order"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutomationStepExecutionsRequest:
    out: DescribeAutomationStepExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "AutomationExecutionId" in data:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    else:
        raise DeserializationError(
            "DescribeAutomationStepExecutionsRequest.automation_execution_id required"
        )
    if "Filters" in data:
        import aws_sdk_ssm.types.step_execution_filter_list

        out["filters"] = (
            aws_sdk_ssm.types.step_execution_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ReverseOrder" in data:
        out["reverse_order"] = data["ReverseOrder"]
    return out
