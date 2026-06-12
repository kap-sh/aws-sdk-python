"""Generated from Smithy shape ``com.amazonaws.swf#DescribeWorkflowExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.workflow_execution


class DescribeWorkflowExecutionInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow execution.</p>"""
    execution: "aws_sdk_swf.types.workflow_execution.WorkflowExecution"
    """<p>The workflow execution to describe.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.workflow_execution

    out["execution"] = aws_sdk_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["execution"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeWorkflowExecutionInput:
    out: DescribeWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("DescribeWorkflowExecutionInput.domain required")
    if "execution" in data:
        import aws_sdk_swf.types.workflow_execution

        out["execution"] = (
            aws_sdk_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["execution"]
            )
        )
    else:
        raise DeserializationError("DescribeWorkflowExecutionInput.execution required")
    return out
