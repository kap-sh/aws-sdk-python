"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeImportTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.import_task_list
    import capo_application_discovery_service.types.next_token


class DescribeImportTasksResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The token to request the next page of results.</p>"""
    tasks: NotRequired[
        "capo_application_discovery_service.types.import_task_list.ImportTaskList"
    ]
    """<p>A returned array of import tasks that match any applied filters, up to the specified number of maximum results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImportTasksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tasks" in value:
        import capo_application_discovery_service.types.import_task_list

        out["tasks"] = (
            capo_application_discovery_service.types.import_task_list.serialize_aws_json_1_1(
                value["tasks"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImportTasksResponse:
    out: DescribeImportTasksResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "tasks" in data:
        import capo_application_discovery_service.types.import_task_list

        out["tasks"] = (
            capo_application_discovery_service.types.import_task_list.deserialize_aws_json_1_1(
                data["tasks"]
            )
        )
    return out
