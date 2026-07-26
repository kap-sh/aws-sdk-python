"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeDataRepositoryTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.data_repository_tasks
    import capo_fsx.types.next_token


class DescribeDataRepositoryTasksResponse(TypedDict, closed=True):
    data_repository_tasks: NotRequired[
        "capo_fsx.types.data_repository_tasks.DataRepositoryTasks"
    ]
    """<p>The collection of data repository task descriptions returned.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataRepositoryTasksResponse) -> dict:
    out: dict = {}
    if "data_repository_tasks" in value:
        import capo_fsx.types.data_repository_tasks

        out["DataRepositoryTasks"] = (
            capo_fsx.types.data_repository_tasks.serialize_aws_json_1_1(
                value["data_repository_tasks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataRepositoryTasksResponse:
    out: DescribeDataRepositoryTasksResponse = {}  # type: ignore[typeddict-item]
    if "DataRepositoryTasks" in data:
        import capo_fsx.types.data_repository_tasks

        out["data_repository_tasks"] = (
            capo_fsx.types.data_repository_tasks.deserialize_aws_json_1_1(
                data["DataRepositoryTasks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
