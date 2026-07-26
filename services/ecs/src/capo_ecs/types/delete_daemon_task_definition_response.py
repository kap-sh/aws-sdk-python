"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonTaskDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DeleteDaemonTaskDefinitionResponse(TypedDict, closed=True):
    daemon_task_definition_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the deleted daemon task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDaemonTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "daemon_task_definition_arn" in value:
        out["daemonTaskDefinitionArn"] = value["daemon_task_definition_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDaemonTaskDefinitionResponse:
    out: DeleteDaemonTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "daemonTaskDefinitionArn" in data:
        out["daemon_task_definition_arn"] = data["daemonTaskDefinitionArn"]
    return out
