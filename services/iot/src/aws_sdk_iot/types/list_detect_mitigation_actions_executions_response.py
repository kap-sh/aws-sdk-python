"""Generated from Smithy shape ``com.amazonaws.iot#ListDetectMitigationActionsExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.detect_mitigation_action_execution_list
    import aws_sdk_iot.types.next_token


class ListDetectMitigationActionsExecutionsResponse(TypedDict, closed=True):
    actions_executions: NotRequired[
        "aws_sdk_iot.types.detect_mitigation_action_execution_list.DetectMitigationActionExecutionList"
    ]
    """<p> List of actions executions. </p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectMitigationActionsExecutionsResponse) -> dict:
    out: dict = {}
    if "actions_executions" in value:
        import aws_sdk_iot.types.detect_mitigation_action_execution_list

        out["actionsExecutions"] = (
            aws_sdk_iot.types.detect_mitigation_action_execution_list.serialize_json(
                value["actions_executions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDetectMitigationActionsExecutionsResponse:
    out: ListDetectMitigationActionsExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "actionsExecutions" in data:
        import aws_sdk_iot.types.detect_mitigation_action_execution_list

        out["actions_executions"] = (
            aws_sdk_iot.types.detect_mitigation_action_execution_list.deserialize_json(
                data["actionsExecutions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
