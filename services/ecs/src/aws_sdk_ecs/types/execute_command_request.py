"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.string


class ExecuteCommandRequest(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) or short name of the cluster the task is running in. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container to execute the command on. A container name only needs to be specified for tasks containing multiple containers.</p>"""
    command: "aws_sdk_ecs.types.string.String"
    """<p>The command to run on the container.</p>"""
    interactive: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Use this flag to run your command in interactive mode.</p>"""
    task: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) or ID of the task the container is part of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteCommandRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "container" in value:
        out["container"] = value["container"]
    out["command"] = value["command"]
    out["interactive"] = value.get("interactive", False)
    out["task"] = value["task"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteCommandRequest:
    out: ExecuteCommandRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "container" in data:
        out["container"] = data["container"]
    if "command" in data:
        out["command"] = data["command"]
    else:
        raise DeserializationError("ExecuteCommandRequest.command required")
    if "interactive" in data:
        out["interactive"] = data["interactive"]
    else:
        out["interactive"] = False
    if "task" in data:
        out["task"] = data["task"]
    else:
        raise DeserializationError("ExecuteCommandRequest.task required")
    return out
