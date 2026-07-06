"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeleteDaemonTaskDefinitionRequest(TypedDict, closed=True):
    daemon_task_definition: "aws_sdk_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the daemon task definition to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDaemonTaskDefinitionRequest) -> dict:
    out: dict = {}
    out["daemonTaskDefinition"] = value["daemon_task_definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDaemonTaskDefinitionRequest:
    out: DeleteDaemonTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "daemonTaskDefinition" in data:
        out["daemon_task_definition"] = data["daemonTaskDefinition"]
    else:
        raise DeserializationError(
            "DeleteDaemonTaskDefinitionRequest.daemon_task_definition required"
        )
    return out
