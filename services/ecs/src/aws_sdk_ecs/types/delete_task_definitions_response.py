"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteTaskDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.task_definition_list


class DeleteTaskDefinitionsResponse(TypedDict, closed=True):
    task_definitions: NotRequired[
        "aws_sdk_ecs.types.task_definition_list.TaskDefinitionList"
    ]
    """<p>The list of deleted task definitions.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTaskDefinitionsResponse) -> dict:
    out: dict = {}
    if "task_definitions" in value:
        import aws_sdk_ecs.types.task_definition_list

        out["taskDefinitions"] = (
            aws_sdk_ecs.types.task_definition_list.serialize_aws_json_1_1(
                value["task_definitions"]
            )
        )
    if "failures" in value:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTaskDefinitionsResponse:
    out: DeleteTaskDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "taskDefinitions" in data:
        import aws_sdk_ecs.types.task_definition_list

        out["task_definitions"] = (
            aws_sdk_ecs.types.task_definition_list.deserialize_aws_json_1_1(
                data["taskDefinitions"]
            )
        )
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
