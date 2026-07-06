"""Generated from Smithy shape ``com.amazonaws.swf#CountPendingActivityTasksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.task_list


class CountPendingActivityTasksInput(TypedDict, closed=True):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain that contains the task list.</p>"""
    task_list: "aws_sdk_swf.types.task_list.TaskList"
    """<p>The name of the task list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountPendingActivityTasksInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.task_list

    out["taskList"] = aws_sdk_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountPendingActivityTasksInput:
    out: CountPendingActivityTasksInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("CountPendingActivityTasksInput.domain required")
    if "taskList" in data:
        import aws_sdk_swf.types.task_list

        out["task_list"] = aws_sdk_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError("CountPendingActivityTasksInput.task_list required")
    return out
