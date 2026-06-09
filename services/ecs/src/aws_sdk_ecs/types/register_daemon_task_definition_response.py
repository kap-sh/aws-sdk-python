"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterDaemonTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class RegisterDaemonTaskDefinitionResponse(TypedDict):
    daemon_task_definition_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the registered daemon task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDaemonTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "daemon_task_definition_arn" in value:
        out["daemonTaskDefinitionArn"] = value["daemon_task_definition_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDaemonTaskDefinitionResponse:
    out: RegisterDaemonTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "daemonTaskDefinitionArn" in data:
        out["daemon_task_definition_arn"] = data["daemonTaskDefinitionArn"]
    return out
