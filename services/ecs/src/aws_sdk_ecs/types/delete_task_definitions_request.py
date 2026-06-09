"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteTaskDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class DeleteTaskDefinitionsRequest(TypedDict):
    task_definitions: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to delete. You must specify a <code>revision</code>.</p> <p>You can specify up to 10 task definitions as a comma separated list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTaskDefinitionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.string_list

    out["taskDefinitions"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
        value["task_definitions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTaskDefinitionsRequest:
    out: DeleteTaskDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "taskDefinitions" in data:
        import aws_sdk_ecs.types.string_list

        out["task_definitions"] = (
            aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
                data["taskDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteTaskDefinitionsRequest.task_definitions required"
        )
    return out
