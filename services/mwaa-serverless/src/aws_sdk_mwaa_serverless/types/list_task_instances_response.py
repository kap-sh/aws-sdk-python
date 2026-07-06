"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListTaskInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.task_instance_summaries


class ListTaskInstancesResponse(TypedDict, closed=True):
    task_instances: NotRequired[
        "aws_sdk_mwaa_serverless.types.task_instance_summaries.TaskInstanceSummaries"
    ]
    """<p>A list of task instance summaries for the specified workflow run.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is null if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTaskInstancesResponse) -> dict:
    out: dict = {}
    if "task_instances" in value:
        import aws_sdk_mwaa_serverless.types.task_instance_summaries

        out["TaskInstances"] = (
            aws_sdk_mwaa_serverless.types.task_instance_summaries.serialize_aws_json_1_0(
                value["task_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTaskInstancesResponse:
    out: ListTaskInstancesResponse = {}  # type: ignore[typeddict-item]
    if "TaskInstances" in data:
        import aws_sdk_mwaa_serverless.types.task_instance_summaries

        out["task_instances"] = (
            aws_sdk_mwaa_serverless.types.task_instance_summaries.deserialize_aws_json_1_0(
                data["TaskInstances"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
