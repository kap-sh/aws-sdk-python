"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterDaemonTaskDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class RegisterDaemonTaskDefinitionResponse(TypedDict, closed=True):
    daemon_task_definition_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the registered daemon task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDaemonTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "daemon_task_definition_arn" in value:
        out["daemonTaskDefinitionArn"] = value["daemon_task_definition_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDaemonTaskDefinitionResponse:
    out: RegisterDaemonTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("daemonTaskDefinitionArn") is not None:
        out["daemon_task_definition_arn"] = data["daemonTaskDefinitionArn"]
    return out
