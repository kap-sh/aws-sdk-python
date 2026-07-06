"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.session
    import aws_sdk_ecs.types.string


class ExecuteCommandResponse(TypedDict, closed=True):
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    container_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the container.</p>"""
    container_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    interactive: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether the execute command session is running in interactive mode. Amazon ECS only supports initiating interactive sessions, so you must specify <code>true</code> for this value.</p>"""
    session: NotRequired["aws_sdk_ecs.types.session.Session"]
    """<p>The details of the SSM session that was created for this instance of execute-command.</p>"""
    task_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteCommandResponse) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "container_arn" in value:
        out["containerArn"] = value["container_arn"]
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    out["interactive"] = value.get("interactive", False)
    if "session" in value:
        import aws_sdk_ecs.types.session

        out["session"] = aws_sdk_ecs.types.session.serialize_aws_json_1_1(
            value["session"]
        )
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteCommandResponse:
    out: ExecuteCommandResponse = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "containerArn" in data:
        out["container_arn"] = data["containerArn"]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    if "interactive" in data:
        out["interactive"] = data["interactive"]
    else:
        out["interactive"] = False
    if "session" in data:
        import aws_sdk_ecs.types.session

        out["session"] = aws_sdk_ecs.types.session.deserialize_aws_json_1_1(
            data["session"]
        )
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    return out
