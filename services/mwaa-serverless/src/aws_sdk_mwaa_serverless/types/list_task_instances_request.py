"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListTaskInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.workflow_arn


class ListTaskInstancesRequest(TypedDict):
    workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>"""
    run_id: "aws_sdk_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the workflow run for which you want a list of task instances.</p>"""
    max_results: "int"
    """<p>The maximum number of task instances to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListTaskInstances</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTaskInstancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTaskInstancesRequest:
    out: ListTaskInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
