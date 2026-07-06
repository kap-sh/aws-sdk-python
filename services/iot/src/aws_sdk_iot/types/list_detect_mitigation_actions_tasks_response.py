"""Generated from Smithy shape ``com.amazonaws.iot#ListDetectMitigationActionsTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.detect_mitigation_actions_task_summary_list
    import aws_sdk_iot.types.next_token


class ListDetectMitigationActionsTasksResponse(TypedDict, closed=True):
    tasks: NotRequired[
        "aws_sdk_iot.types.detect_mitigation_actions_task_summary_list.DetectMitigationActionsTaskSummaryList"
    ]
    """<p> The collection of ML Detect mitigation tasks that matched the filter criteria. </p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectMitigationActionsTasksResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import aws_sdk_iot.types.detect_mitigation_actions_task_summary_list

        out["tasks"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_summary_list.serialize_json(
                value["tasks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDetectMitigationActionsTasksResponse:
    out: ListDetectMitigationActionsTasksResponse = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_iot.types.detect_mitigation_actions_task_summary_list

        out["tasks"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_summary_list.deserialize_json(
                data["tasks"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
