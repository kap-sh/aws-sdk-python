"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.task_definition


class RegisterTaskDefinitionResponse(TypedDict):
    task_definition: NotRequired["aws_sdk_ecs.types.task_definition.TaskDefinition"]
    """<p>The full description of the registered task definition.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The list of tags associated with the task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "task_definition" in value:
        import aws_sdk_ecs.types.task_definition

        out["taskDefinition"] = (
            aws_sdk_ecs.types.task_definition.serialize_aws_json_1_1(
                value["task_definition"]
            )
        )
    if "tags" in value:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterTaskDefinitionResponse:
    out: RegisterTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "taskDefinition" in data:
        import aws_sdk_ecs.types.task_definition

        out["task_definition"] = (
            aws_sdk_ecs.types.task_definition.deserialize_aws_json_1_1(
                data["taskDefinition"]
            )
        )
    if "tags" in data:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
