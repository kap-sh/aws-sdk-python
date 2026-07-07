"""Generated from Smithy shape ``com.amazonaws.ecs#DeregisterTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeregisterTaskDefinitionRequest(TypedDict, closed=True):
    task_definition: "aws_sdk_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a <code>revision</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTaskDefinitionRequest) -> dict:
    out: dict = {}
    out["taskDefinition"] = value["task_definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterTaskDefinitionRequest:
    out: DeregisterTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "taskDefinition" in data:
        out["task_definition"] = data["taskDefinition"]
    else:
        raise DeserializationError(
            "DeregisterTaskDefinitionRequest.task_definition required"
        )
    return out
