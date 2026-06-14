"""Generated from Smithy shape ``com.amazonaws.swf#PollForActivityTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.identity
    import aws_sdk_swf.types.task_list


class PollForActivityTaskInput(TypedDict):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain that contains the task lists being polled.</p>"""
    task_list: "aws_sdk_swf.types.task_list.TaskList"
    r"""<p>Specifies the task list to poll for activity tasks.</p> <p>The specified string must not start or end with whitespace. It must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    identity: NotRequired["aws_sdk_swf.types.identity.Identity"]
    """<p>Identity of the worker making the request, recorded in the <code>ActivityTaskStarted</code> event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PollForActivityTaskInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_swf.types.task_list

    out["taskList"] = aws_sdk_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "identity" in value:
        out["identity"] = value["identity"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PollForActivityTaskInput:
    out: PollForActivityTaskInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("PollForActivityTaskInput.domain required")
    if "taskList" in data:
        import aws_sdk_swf.types.task_list

        out["task_list"] = aws_sdk_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError("PollForActivityTaskInput.task_list required")
    if "identity" in data:
        out["identity"] = data["identity"]
    return out
