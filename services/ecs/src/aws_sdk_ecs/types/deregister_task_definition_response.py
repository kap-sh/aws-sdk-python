"""Generated from Smithy shape ``com.amazonaws.ecs#DeregisterTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_definition


class DeregisterTaskDefinitionResponse(TypedDict):
    task_definition: NotRequired["aws_sdk_ecs.types.task_definition.TaskDefinition"]
    """<p>The full description of the deregistered task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "task_definition" in value:
        import aws_sdk_ecs.types.task_definition

        out["taskDefinition"] = (
            aws_sdk_ecs.types.task_definition.serialize_aws_json_1_1(
                value["task_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterTaskDefinitionResponse:
    out: DeregisterTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "taskDefinition" in data:
        import aws_sdk_ecs.types.task_definition

        out["task_definition"] = (
            aws_sdk_ecs.types.task_definition.deserialize_aws_json_1_1(
                data["taskDefinition"]
            )
        )
    return out
